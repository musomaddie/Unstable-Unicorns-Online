import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class AnnoyingFlyingUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.unicorn = find_card_in_db("Annoying Flying Unicorn")

    def test_basic_example(self):
        result = gm._handle_card_play(gm.PLAYERS[0], self.unicorn)
        self.assertFalse(result)

        self.assertEqual(len(gm.PLAYERS[1].hand), 4)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].stable[1].name,
                         "Annoying Flying Unicorn")
