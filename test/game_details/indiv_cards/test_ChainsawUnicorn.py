import os
import sys
import unittest

from unittest.mock import MagicMock, call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class ChainsawUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        chainsaw = find_card_in_db("Chainsaw Unicorn")
        self.downgrade = find_card_in_db("Barbed Wire")
        gm._make_choice = MagicMock(name="Make Choice",
                                    side_effect=[
                                        1,  # Choose player for downgrade
                                        0,  # Choose card to discard
                                        0]  # Choose upgrade to remove
                                    )
        gm.PLAYERS[0].add_to_hand(self.downgrade)
        gm.PLAYERS[1].add_to_hand(chainsaw)
        gm._handle_card_play(gm.PLAYERS[0], self.downgrade)
        gm._handle_card_play(gm.PLAYERS[1], chainsaw)

    def test_basic_enter(self):
        self.assertEqual(len(gm.PLAYERS[1].stable), 2,
                         "Incorrect number of cards in stable")
        self.assertEqual(gm.PLAYERS[1].num_unicorns, 2,
                         "Incorrect amount of unicorns")
        self.assertTrue("Chainsaw Unicorn" in gm.PLAYERS[1].stable,
                        "The chainsaw unicorn has not been added to the stable"
                        )
        self.assertFalse("Barbed Wire" in gm.PLAYERS[1].stable,
                         "The downgrade card has not left the stable")
        self.assertFalse(gm.PLAYERS[1].unicorn_effects_blocked,
                         "The barbed wire effect has not reset")
        self.assertTrue("Barbed Wire" in gm.DISCARD_PILE,
                        "Barbed Wire has not been sent to the discard pile")

        # Assert mocks
        calls = gm._make_choice.mock_calls
        self.assertEqual(len(calls), 3)
        self.assertEqual(calls[0], call(gm.PLAYERS))
        self.assertEqual(calls[2], call([self.downgrade]))
