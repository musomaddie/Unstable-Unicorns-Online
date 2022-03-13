import os
import sys
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class DragonTurtleUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm.PLAYERS[0].add_to_hand(find_card_in_db("Dragon Turtle Unicorn"))
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Dragon Turtle Unicorn"))

    def test_basic_example(self):
        self.assertTrue("Dragon Turtle Unicorn" in gm.PLAYERS[0].stable,
                        "Dragon Turtle Unicorn not added to stable")
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "Drawn card not added to hand")
