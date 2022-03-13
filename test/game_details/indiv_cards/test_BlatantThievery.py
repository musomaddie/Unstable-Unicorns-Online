import copy
import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class BlatantThieveryTests(unittest.TestCase):
    # TODO: not sure how best to handle this once the hardcoded examples for
    # the choice methods are removed or changed.

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm.PLAYERS[0].add_to_hand("Blatant Thievery")
        self.blatant_thievery = find_card_in_db("Blatant Thievery")
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=1)
        self.original_hand = copy.copy(gm.PLAYERS[1].hand)
        gm._handle_card_play(gm.PLAYERS[0], self.blatant_thievery)

    def test_basic_use(self):
        # Confirm change
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "The player has not gained a card")
        self.assertEqual(len(gm.PLAYERS[1].hand), 4,
                         "The player has not lost a card")
        self.assertEqual(len(gm.DISCARD_PILE), 1,
                         "Blatant Thievery has not moved to the discard pile")

        # Should be called twice
        calls = gm._make_choice.mock_calls
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0], call(gm.PLAYERS))
        self.assertEqual(calls[1], call(self.original_hand))
