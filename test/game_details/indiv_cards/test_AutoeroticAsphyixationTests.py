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


class AutoeroticAsphyixationTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        gm.PLAYERS[0].add_to_hand(find_card_in_db("Autoerotic Asphyxiation"))
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Autoerotic Asphyxiation"))

    def test_basic(self):
        # Assert call on magic mock
        gm._make_choice.assert_called_once_with(gm.PLAYERS)
        orig_hand = copy.copy(gm.PLAYERS[0].hand)

        gm._handle_beginning_turn_action(gm.PLAYERS[0])
        self.assertEqual(len(gm.PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(len(gm.DISCARD_PILE), 1)
        self.assertEqual(len(gm._make_choice.mock_calls), 2)
        self.assertEqual(gm._make_choice.mock_calls[1], call(orig_hand))
