import copy
import os
import sys
import unittest

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from game_details.CardLocation import CardLocation
from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class AngelUnicornTests(unittest.TestCase):
    # TODO: slight issue in that it allows the players to choose the same angel
    # unicorn
    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.basic_unicorn = find_card_in_db("Basic Unicorn (2)")
        angel_unicorn = find_card_in_db("Angel Unicorn")
        gm.DISCARD_PILE.append(copy.copy(self.basic_unicorn))
        gm._handle_card_play(gm.PLAYERS[0], angel_unicorn)

    def test_basic_example(self):
        # Setting up the mocks and performing action
        gm._confirm_proceed = MagicMock(name="Confirm Proceed",
                                        return_value=True)
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_beginning_turn_action(gm.PLAYERS[0])

        # Check the mock stages
        gm._confirm_proceed.assert_called_once()
        gm._make_choice.assert_called_once_with(
            ["Basic Unicorn (2)", "Angel Unicorn"])

        # Check the game conditions
        self.assertEqual(len(gm.DISCARD_PILE), 1)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.DISCARD_PILE[0].name, "Angel Unicorn")
        self.assertEqual(gm.PLAYERS[0].stable[1].name, "Basic Unicorn (2)")
        self.assertEqual(gm.DISCARD_PILE[0].location,
                         CardLocation.DISCARD_PILE)
