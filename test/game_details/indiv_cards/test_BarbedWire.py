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


class BarbedWireTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.barbed_wire = find_card_in_db("Barbed Wire")
        self.basic = find_card_in_db("Apprentice Unicorn")
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.barbed_wire)

    def test_basic(self):
        # First test what happens when a unicorn is played
        expected_hand = copy.copy(gm.PLAYERS[0].hand)
        gm._handle_card_play(gm.PLAYERS[0], self.basic)

        self.assertEqual(len(gm.PLAYERS[0].stable), 3)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(gm.PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.DISCARD_PILE), 1)
        self.assertEqual(len(gm._make_choice.mock_calls), 2)
        self.assertEqual(gm._make_choice.mock_calls[0], call(gm.PLAYERS))
        self.assertEqual(gm._make_choice.mock_calls[1], call(expected_hand))

        # Test what happens when unicorn is removed
        expected_hand = copy.copy(gm.PLAYERS[0].hand)
        gm._handle_leave_stable([gm.PLAYERS[0], self.basic, None])
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)
        # This is only 2 as handle_leave_stable doesn't directly add to
        # DISCARD pile
        self.assertEqual(len(gm.DISCARD_PILE), 2)
        self.assertEqual(len(gm._make_choice.mock_calls), 3)
        self.assertEqual(gm._make_choice.mock_calls[2], call(expected_hand))

        # Then remove barbed wire (will not discard in addition)
        gm._handle_leave_stable([gm.PLAYERS[0], self.barbed_wire, None])
        self.assertEqual(len(gm.PLAYERS[0].stable), 1)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)
        self.assertEqual(len(gm.DISCARD_PILE), 2)
        self.assertEqual(len(gm._make_choice.mock_calls), 3)

        # Play unicorn again
        gm._handle_card_play(gm.PLAYERS[0], self.basic)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)
        self.assertEqual(len(gm._make_choice.mock_calls), 3)
