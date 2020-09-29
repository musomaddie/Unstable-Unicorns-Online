import os
import sys
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BlackKnightUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.black_knight = find_card_in_db("Black Knight Unicorn")

    def test_value_change(self):
        self.assertFalse(gm.PLAYERS[0].unicorn_destroy_decoy)

        gm._handle_card_play(gm.PLAYERS[0], self.black_knight)
        self.assertTrue(gm.PLAYERS[0].unicorn_destroy_decoy,
                        "Black Knight Unicorn effect not applied on enter")

        gm._handle_leave_stable([gm.PLAYERS[0], self.black_knight, None])
        self.assertFalse(gm.PLAYERS[0].unicorn_destroy_decoy,
                         "Black Knight Unicorn effect not applied on leave")

    # TODO: write more tests once there is a destroy card implemented
