import copy
import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from game_details.CardLocation import CardLocation
from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class BackKickTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.back_kick = find_card_in_db("Back Kick")
        self.basic = find_card_in_db("Basic Unicorn (1)")

    def test_basic_no_baby(self):
        gm.PLAYERS[1].stable.insert(1, self.basic)
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=1)
        orig_stable = copy.copy(gm.PLAYERS[1].stable)
        orig_hand = copy.copy(gm.PLAYERS[1].hand)
        orig_hand.append(gm.PLAYERS[1].stable[1])

        result = gm._handle_card_play(gm.PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(self.back_kick.location, CardLocation.DISCARD_PILE)
        self.assertEqual(self.basic.location, CardLocation.HAND)
        self.assertEqual(len(gm.PLAYERS[1].stable), 1)
        self.assertEqual(len(gm.PLAYERS[1].hand), 5)

        self.assertEqual(len(gm._make_choice.mock_calls), 3)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS))
        self.assertEqual(gm._make_choice.mock_calls[1],
                         call(orig_stable))
        self.assertEqual(gm._make_choice.mock_calls[2],
                         call(orig_hand))

    def test_basic_only_baby(self):
        old_nursery = len(gm.NURSERY)
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        orig_stable = copy.copy(gm.PLAYERS[0].stable)
        orig_hand = copy.copy(gm.PLAYERS[0].hand)
        result = gm._handle_card_play(gm.PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(len(gm.PLAYERS[0].stable), 0)
        self.assertEqual(len(gm.PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.NURSERY), old_nursery + 1)

        self.assertEqual(len(gm._make_choice.mock_calls), 3)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS))
        self.assertEqual(gm._make_choice.mock_calls[1],
                         call(orig_stable))
        self.assertEqual(gm._make_choice.mock_calls[2],
                         call(orig_hand))
