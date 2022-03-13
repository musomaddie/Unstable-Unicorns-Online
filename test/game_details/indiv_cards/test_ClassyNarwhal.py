import os
import sys
import unittest

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class ClassyNarwhalTests(unittest.TestCase):

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm.PLAYERS[0].add_to_hand(find_card_in_db("Classy Narwhal"))
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Classy Narwhal"))

    def test_basic_example(self):
        self.assertTrue("Classy Narwhal" in gm.PLAYERS[0].stable,
                        "Classy narwhal not added to stable")
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "Upgrade card not added to hand")
        self.assertEqual(gm.PLAYERS[0].hand[5].card_type, "Upgrade",
                         "the most recent card in hand is not an upgrade")

        # assert the mock
        gm._make_choice.assert_called_once()
        call_args = gm._make_choice.call_args
        args, kwargs = call_args
        for item in args[0]:
            self.assertEqual("Upgrade", item.card_type)
