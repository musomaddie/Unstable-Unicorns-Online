import unittest
import sys
import os

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
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Dirty Mind"))

    def test_basic_example(self):
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "NSFW card not added to hand")
        self.assertEqual(gm.PLAYERS[0].hand[5].deck, "Uncut",
                         " the most recent card in hand is not a NSFW card")
