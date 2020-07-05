import os
import sys
import unittest

from unittest.mock import MagicMock, call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class DominatrixWhipTestsTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Dominatrix Whip"))

    def test_basic_play(self):
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)

    def test_effect(self):
        # Add a unicorn to another players stable
        gm._handle_card_play(gm.PLAYERS[1],
                             find_card_in_db("Basic Unicorn (1)"))
        # Set up the mocks
        gm._confirm_proceed = MagicMock(name="Confirm Proceed",
                                        return_value=True)
        gm._make_choice = MagicMock(name="Make Choice",
                                    side_effect=[1,  # Player from
                                                 2,  # Player to
                                                 1]  # Unicorn
                                    )

        # Save any required states and call the method
        gm._handle_beginning_turn_action(gm.PLAYERS[0])

        # Assert the changes
        self.assertEqual(len(gm.PLAYERS[1].stable), 1,
                         "The unicorn did not leave the stable")
        self.assertEqual(len(gm.PLAYERS[2].stable), 2,
                         "the unicorn did not join the stable")
        self.assertTrue("Basic Unicorn (1)" in gm.PLAYERS[2].stable,
                        "The stable does not contain the moved unicorn")

        # Confirm the use of the mock methods
        gm._confirm_proceed.assert_called_once()
        choice_calls = gm._make_choice.mock_calls
        self.assertEqual(len(choice_calls), 3,
                         "Making choice is called the wrong number of times")
        self.assertEqual(choice_calls[0],
                         call(gm.PLAYERS))
        self.assertEqual(choice_calls[1], call(gm.PLAYERS))
        self.assertEqual(choice_calls[2],
                         call(["Baby Unicorn", "Basic Unicorn (1)"]))

    def test_transfer_baby_unicorns(self):
        gm._confirm_proceed = MagicMock(name="Confirm Proceed",
                                        return_value=True)
        gm._make_choice = MagicMock(name="Make Choice",
                                    side_effect=[0,  # Player from
                                                 1,  # Player to
                                                 0])  # Unicorn

        gm._handle_beginning_turn_action(gm.PLAYERS[0])

        self.assertEqual(len(gm.PLAYERS[0].stable), 1,
                         "The baby unicorn did not leave the stable")
        self.assertEqual(len(gm.PLAYERS[1].stable), 2,
                         "The baby unicorn did not join the stable")
        self.assertEqual(gm.PLAYERS[1].stable[0], "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[1], "Baby Unicorn")

        # Confirm use of mocks
        gm._confirm_proceed.assert_called_once()
        choice_calls = gm._make_choice.mock_calls
        self.assertEqual(len(choice_calls), 3)
        self.assertEqual(choice_calls[0], call(gm.PLAYERS))
        self.assertEqual(choice_calls[1], call(gm.PLAYERS))
        self.assertEqual(choice_calls[2], call(["Baby Unicorn"]))
