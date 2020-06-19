import unittest
import sys
import os
import copy

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class ACuteAttackTests(unittest.TestCase):
    # TODO: not sure how best to handle this once the hardcoded examples for
    # the choice methods are removed or changed.

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        basic_unicorn = find_card_in_db("Basic Unicorn (1)")
        self.a_cute_attack = find_card_in_db("A Cute Attack")
        for i in range(3):
            gm.PLAYERS[1].add_to_stable(copy.copy(basic_unicorn))

    def test_basic_example(self):
        gm._move_to_discard([gm.PLAYERS[0], self.a_cute_attack])
        self.assertEqual(len(gm.PLAYERS[1].stable), 4)
        self.assertEqual(gm.PLAYERS[1].stable[1].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[2].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[3].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].num_unicorns, 4)
