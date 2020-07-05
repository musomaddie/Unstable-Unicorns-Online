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


class AnnoyingFlyingUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.unicorn = find_card_in_db("Annoying Flying Unicorn")

    def test_basic_example(self):
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=1)
        orig_hand = copy.copy(gm.PLAYERS[1].hand)
        result = gm._handle_card_play(gm.PLAYERS[0], self.unicorn)
        self.assertFalse(result)

        self.assertEqual(len(gm.PLAYERS[1].hand), 4)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].stable[1].name,
                         "Annoying Flying Unicorn")
        self.assertEqual(len(gm._make_choice.mock_calls), 2)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS),
                         "The first mock call didn't pass through the players")
        self.assertEqual(gm._make_choice.mock_calls[1],
                         call(orig_hand),
                         "The second mock call didn't contain the original "
                         "hand")
