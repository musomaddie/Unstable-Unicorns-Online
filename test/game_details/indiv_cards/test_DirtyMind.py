import os
import sys
import unittest

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class DirtyMindTests(unittest.TestCase):

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Dirty Mind"))

    def test_basic_example(self):
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "NSFW card not added to hand")
        self.assertEqual(gm.PLAYERS[0].hand[5].deck, "Uncut",
                         " the most recent card in hand is not a NSFW card")

        # Confirm only the correct cards passed
        gm._make_choice.assert_called_once()
        call_args = gm._make_choice.call_args
        args, kwargs = call_args
        for item in args[0]:
            self.assertEqual("Uncut", item.deck)
