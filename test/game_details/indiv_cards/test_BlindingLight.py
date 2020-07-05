import os
import sys
import unittest

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BlindingLightTests(unittest.TestCase):
    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.blinding_light = find_card_in_db("Blinding Light")

    def test_original_play_and_leave(self):
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        # Play the card (player 0)
        gm._handle_card_play(gm.PLAYERS[0], self.blinding_light)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2,
                         "There is the wrong number of cards in the stable")
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1,
                         "Player 0 has the wrong number of unicorns")
        self.assertTrue(gm.PLAYERS[0].unicorn_effects_blocked,
                        "The effect has not switched")

        gm._handle_leave_stable([gm.PLAYERS[0], self.blinding_light, None])
        self.assertFalse(gm.PLAYERS[0].unicorn_effects_blocked)

        gm._make_choice.assert_called_once_with(gm.PLAYERS)

    def test_effect_unicorn_on_enter(self):
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.blinding_light)

        # Play a unicorn card
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db(
            "Bear Daddy Unicorn"))

        self.assertEqual(len(gm.PLAYERS[0].stable), 3,
                         "The unicorn was not added to the stable")
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2,
                         "The number of unicorns did not increase")
        self.assertEqual(len(gm.PLAYERS[0].hand), 5,
                         "The unicorn effect DID activate :(")

        # The mock should only be called once as the search should never happen
        gm._make_choice.assert_called_once_with(gm.PLAYERS)

    # TODO: more thorough tests later!
    # Test use of effects on removal (if valid)
    # Test does not effect upgrades / downgrades
    # Test does not effect pandas
