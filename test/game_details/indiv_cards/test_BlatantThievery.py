import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BlatantThieveryTests(unittest.TestCase):
    # TODO: not sure how best to handle this once the hardcoded examples for
    # the choice methods are removed or changed.

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.blatant_thievery = find_card_in_db("Blatant Thievery")

    def test_basic_use(self):
        # Confirm starting statistics
        self.assertEqual(len(gm.PLAYERS[0].hand), 5,
                         "The first player does not start with the "
                         "correct number of cards")
        self.assertEqual(len(gm.PLAYERS[1].hand), 5,
                         "The second player does not start with the "
                         "correct number of cards")
        self.assertEqual(len(gm.DISCARD_PILE), 0,
                         "The discard pile already contains a card")
        first_card = gm.PLAYERS[1].hand[0]

        # Play the card
        gm._handle_card_play(gm.PLAYERS[0], self.blatant_thievery)

        # Confirm change
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "The player has not gained a card")
        self.assertEqual(len(gm.PLAYERS[1].hand), 4,
                         "The player has not lost a card")
        self.assertEqual(len(gm.DISCARD_PILE), 1,
                         "Blatant Thievery has not moved to the discard pile")
