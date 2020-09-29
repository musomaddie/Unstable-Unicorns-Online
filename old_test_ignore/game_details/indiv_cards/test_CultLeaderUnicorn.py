import os
import sys
import unittest

from unittest.mock import MagicMock, call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class CultLeaderUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(name="Make Choice", return_value=0)
        self.original_hands = [player.stable for player in gm.PLAYERS]
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Cult Leader Unicorn"))

    def test_basic_play(self):
        self.assertEqual(len(gm.PLAYERS[0].stable), 1,
                         "Player 0's stable has the wrong number of unicorns")
        for i in range(1, 3):
            self.assertEqual(len(gm.PLAYERS[i].stable), 0,
                             f"Player {i}'s stable has the wrong number of "
                             "unicorns")

        # Assert that all the unicorns were passed
        calls = gm._make_choice.mock_calls
        self.assertEqual(len(calls), 3)
        self.assertEqual(calls[0],
                         call(["Baby Unicorn", "Cult Leader Unicorn"]))
        for i in range(1, 3):
            self.assertEqual(calls[i], call(["Baby Unicorn"]))
