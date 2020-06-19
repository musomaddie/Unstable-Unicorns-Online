import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BackKickTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.back_kick = find_card_in_db("Back Kick")
        self.basic = find_card_in_db("Basic Unicorn (1)")

    def test_basic_no_baby(self):
        gm.PLAYERS[1].stable.insert(0, self.basic)
        result = gm._handle_card_play(gm.PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(len(gm.PLAYERS[1].stable), 1)
        self.assertEqual(len(gm.PLAYERS[1].hand), 5)

    def test_basic_only_baby(self):
        old_nursery = len(gm.NURSERY)
        result = gm._handle_card_play(gm.PLAYERS[0], self.back_kick)
        self.assertFalse(result)

        self.assertEqual(len(gm.PLAYERS[1].stable), 0)
        self.assertEqual(len(gm.PLAYERS[1].hand), 4)
        self.assertEqual(len(gm.NURSERY), old_nursery + 1)
