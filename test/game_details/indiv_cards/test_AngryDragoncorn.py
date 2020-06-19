import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class AngryDragoncornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.angry_dragoncorn = find_card_in_db("Angry Dragoncorn")

    def test_basic_example(self):
        self.assertEqual(len(gm.DISCARD_PILE), 0)
        for player in gm.PLAYERS:
            self.assertEqual(len(player.hand), 5)

        result = gm._handle_card_play(gm.PLAYERS[0], self.angry_dragoncorn)
        self.assertFalse(result)
        self.assertEqual(len(gm.DISCARD_PILE), 3)

        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].stable[1].name, "Angry Dragoncorn")

        for player in gm.PLAYERS:
            self.assertEqual(len(player.hand), 4)
