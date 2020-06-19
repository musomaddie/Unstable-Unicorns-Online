import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class AutoeroticAsphyixationTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        card = find_card_in_db("Autoerotic Asphyxiation")
        gm.PLAYERS[0].add_to_stable(card)

    def test_basic(self):
        gm._handle_beginning_turn_action(gm.PLAYERS[0])
        self.assertEqual(len(gm.PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(len(gm.DISCARD_PILE), 1)
