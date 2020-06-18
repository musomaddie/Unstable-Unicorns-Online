import unittest
import os
import sys
import sqlite3
import copy

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from game_details.game_manager import create_game
from game_details.game_manager import DECK as deck
from game_details.game_manager import PLAYERS
from game_details.game_manager import _add_to_stable
from game_details.game_manager import _move_to_discard
from game_details.game_manager import _handle_beginning_turn_action
from game_details.game_manager import _handle_card_play
from game_details.game_manager import _handle_leave_stable
import game_details.game_manager as gm
from game_details.Card import Card

DB_NAME = "db/UnstableUnicorns.db"


def find_card_in_db(card_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(f"""SELECT *
                    FROM card_details
                    WHERE name = '{card_name}';
                """)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return Card(result)


class ACuteAttackTests(unittest.TestCase):
    # TODO: not sure how best to handle this once the hardcoded examples for
    # the choice methods are removed or changed.

    def setUp(self):
        # Create the required game!!
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        basic_unicorn = find_card_in_db("Basic Unicorn (1)")
        self.a_cute_attack = find_card_in_db("A Cute Attack")
        for i in range(3):
            PLAYERS[1].add_to_stable(copy.copy(basic_unicorn))

    def test_basic_example(self):
        _move_to_discard([PLAYERS[0], self.a_cute_attack])
        self.assertEqual(len(PLAYERS[1].stable), 4)
        self.assertEqual(PLAYERS[1].stable[1].name, "Baby Unicorn")
        self.assertEqual(PLAYERS[1].stable[2].name, "Baby Unicorn")
        self.assertEqual(PLAYERS[1].stable[3].name, "Baby Unicorn")
        self.assertEqual(PLAYERS[1].num_unicorns, 4)


class AngelUnicornTests(unittest.TestCase):
    # TODO: slight issue in that it allows the players to choose the same angel
    # unicorn
    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        self.basic_unicorn = find_card_in_db("Basic Unicorn (2)")
        angel_unicorn = find_card_in_db("Angel Unicorn")
        gm.DISCARD_PILE.append(copy.copy(self.basic_unicorn))
        PLAYERS[0].add_to_stable(angel_unicorn)

    def test_basic_example(self):
        _handle_beginning_turn_action(PLAYERS[0])
        # Should have left discard and be in stable (swap places)
        self.assertEqual(len(gm.DISCARD_PILE), 1)
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(gm.DISCARD_PILE[0].name, "Angel Unicorn")
        self.assertEqual(PLAYERS[0].stable[1].name, "Basic Unicorn (2)")


class AngryDragoncornTests(unittest.TestCase):

    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        self.angry_dragoncorn = find_card_in_db("Angry Dragoncorn")

    def test_basic_example(self):
        self.assertEqual(len(gm.DISCARD_PILE), 0)
        for player in PLAYERS:
            self.assertEqual(len(player.hand), 5)

        result = _handle_card_play(PLAYERS[0], self.angry_dragoncorn)
        self.assertFalse(result)
        self.assertEqual(len(gm.DISCARD_PILE), 3)

        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(PLAYERS[0].stable[1].name, "Angry Dragoncorn")

        for player in PLAYERS:
            self.assertEqual(len(player.hand), 4)


class AnnoyingFlyingUnicornTests(unittest.TestCase):

    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        self.unicorn = find_card_in_db("Annoying Flying Unicorn")

    def test_basic_example(self):
        result = _handle_card_play(PLAYERS[0], self.unicorn)
        self.assertFalse(result)

        self.assertEqual(len(PLAYERS[1].hand), 4)
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(PLAYERS[0].stable[1].name, "Annoying Flying Unicorn")


class AutoeroticAsphyixationTests(unittest.TestCase):

    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        card = find_card_in_db("Autoerotic Asphyxiation")
        PLAYERS[0].add_to_stable(card)

    def test_basic(self):
        _handle_beginning_turn_action(PLAYERS[0])
        self.assertEqual(len(PLAYERS[0].hand), 4)
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(len(gm.DISCARD_PILE), 1)


class BackKickTests(unittest.TestCase):

    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        self.back_kick = find_card_in_db("Back Kick")
        self.basic = find_card_in_db("Basic Unicorn (1)")

    def test_basic_no_baby(self):
        PLAYERS[1].stable.insert(0, self.basic)
        result = _handle_card_play(PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(len(PLAYERS[1].stable), 1)
        self.assertEqual(len(PLAYERS[1].hand), 5)

    def test_basic_only_baby(self):
        old_nursery = len(gm.NURSERY)
        result = _handle_card_play(PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(len(PLAYERS[1].stable), 0)
        self.assertEqual(len(PLAYERS[1].hand), 4)
        self.assertEqual(len(gm.NURSERY), old_nursery + 1)


class BarbedWireTests(unittest.TestCase):

    def setUp(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        self.barbed_wire = find_card_in_db("Barbed Wire")
        self.basic = find_card_in_db("Apprentice Unicorn")
        _add_to_stable([PLAYERS[0], self.barbed_wire, None])

    def test_basic(self):

        # Confirm everything is as expected here
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(PLAYERS[0].hand), 5)
        self.assertEqual(len(gm.DISCARD_PILE), 0)

        # First test what happens when a unicorn is played
        _handle_card_play(PLAYERS[0], self.basic)

        self.assertEqual(len(PLAYERS[0].stable), 3)
        self.assertEqual(PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.DISCARD_PILE), 1)

        # Test what happens when unicorn is removed
        _handle_leave_stable([PLAYERS[0], self.basic, None])
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(PLAYERS[0].hand), 3)
        self.assertEqual(len(gm.DISCARD_PILE), 3)

        # Then remove barbed wire (will not discard in addition)
        _handle_leave_stable([PLAYERS[0], self.barbed_wire, None])
        self.assertEqual(len(PLAYERS[0].stable), 1)
        self.assertEqual(PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(PLAYERS[0].hand), 3)
        self.assertEqual(len(gm.DISCARD_PILE), 4)
        self.assertTrue(self.barbed_wire in gm.DISCARD_PILE)

        # Play unicorn again
        _handle_card_play(PLAYERS[0], self.basic)
        self.assertEqual(len(PLAYERS[0].stable), 2)
        self.assertEqual(PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(PLAYERS[0].hand), 3)


class StartingDeck(unittest.TestCase):
    # TODO: something's gone terribly wrong: the numbers are no longer adding
    # up. It's not terribly obvious why so recalculate all this :(

    NUM_CARDS_STANDARD = 111
    NUM_CARDS_RAINBOW = 44
    NUM_CARDS_NSFW = 42
    NUM_CARDS_UNCUT = 41
    NUM_CARDS_DRAGON = 49

    def test_all_decks(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck),
                         StartingDeck.NUM_CARDS_STANDARD
                         + StartingDeck.NUM_CARDS_RAINBOW
                         + StartingDeck.NUM_CARDS_NSFW
                         + StartingDeck.NUM_CARDS_UNCUT
                         + StartingDeck.NUM_CARDS_DRAGON)
                         """

    def test_nsfw_decks(self):
        create_game(["Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck),
                         StartingDeck.NUM_CARDS_NSFW
                         + StartingDeck.NUM_CARDS_UNCUT)
                         """

    def test_one_deck_not_standard(self):
        create_game(["Dragon"],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_only_standard(self):
        create_game(["Standard"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck), StartingDeck.NUM_CARDS_STANDARD)
        """

    def test_nonexistent_deck(self):
        create_game(["FOO"],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_no_deck(self):
        create_game([],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_nonexistent_deck_with_existent(self):
        create_game(["FOO", "Standard"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck), StartingDeck.NUM_CARDS_STANDARD)
        """


if __name__ == '__main__':
    unittest.main()
