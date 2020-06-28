import unittest
import sys
import os

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class DominatrixWhipTestsTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._choose_player_choice_made = MagicMock(return_value=gm.PLAYERS[0])
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Dominatrix Whip"))

    def test_basic_play(self):
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        gm._choose_player_choice_made.assert_called_once()

    def test_effect(self):
        # Add a unicorn to another players stable
        gm._handle_card_play(gm.PLAYERS[1],
                             find_card_in_db("Basic Unicorn (1)"))
        # Mock the choice of unicorn
        gm._choose_unicorn_choice_made = MagicMock(
            return_value=gm.PLAYERS[1].stable[1])

        # Mock the player selection
        gm._choose_player_choice_made = MagicMock(side_effect=[gm.PLAYERS[1],
                                                               gm.PLAYERS[2]])

        gm._check_proceed_with_action.get_result = MagicMock(return_value=True)

        # Perform the operation
        gm._handle_beginning_turn_action(gm.PLAYERS[0])

        # Assert the changes
        self.assertEqual(len(gm.PLAYERS[1].stable), 1,
                         "The unicorn did not leave the stable")
        self.assertEqual(len(gm.PLAYERS[2].stable), 2,
                         "the unicorn did not join the stable")
        self.assertTrue("Basic Unicorn (1)" in gm.PLAYERS[2].stable,
                        "The stable does not contain the moved unicorn")

        # TODO: Assert correct calls of mocks

    def test_transfer_baby_unicorns(self):
        gm._choose_unicorn_choice_made = MagicMock(
            return_value=gm.PLAYERS[0].stable[0])
        gm._choose_player_choice_made = MagicMock(side_effect=[gm.PLAYERS[0],
                                                               gm.PLAYERS[1]])

        gm._handle_beginning_turn_action(gm.PLAYERS[0])

        self.assertEqual(len(gm.PLAYERS[0].stable), 1,
                         "The baby unicorn did not leave the stable")
        self.assertEqual(len(gm.PLAYERS[1].stable), 2,
                         "The baby unicorn did not join the stable")
        self.assertEqual(gm.PLAYERS[1].stable[0], "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[1], "Baby Unicorn")
