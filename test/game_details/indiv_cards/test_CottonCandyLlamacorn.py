import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class CottonCandyLlamacornTests(unittest.TestCase):

    def setUp(self):
        # Create the required game!!
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Cotton Candy Llamacorn"))

    def test_basic_play(self):
        self.assertEqual(len(gm.PLAYERS[0].stable), 1,
                         "player 0's stable is the wrong length")
        self.assertTrue("Cotton Candy Llamacorn" in gm.PLAYERS[0].stable,
                        "Stable does not contain the played card")
        for i in range(1, 3):
            self.assertEqual(len(gm.PLAYERS[i].stable), 0,
                             f"Player {i}'s stable is the wrong length")
        for i in range(3):
            self.assertEqual(len(gm.PLAYERS[i].hand), 6,
                             f"Player {i} did not draw a card")
