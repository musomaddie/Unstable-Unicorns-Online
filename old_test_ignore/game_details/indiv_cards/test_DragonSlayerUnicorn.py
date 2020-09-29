import os
import sys
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class DragonSlayerUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Dragon Slayer Unicorn"))

    def test_enter_effect(self):
        self.assertTrue(gm.PLAYERS[0].protected_from_dragons)

    def test_leave_effect(self):
        gm._handle_leave_stable([gm.PLAYERS[0],
                                 find_card_in_db("Dragon Slayer Unicorn"),
                                 None])
        self.assertFalse(gm.PLAYERS[0].protected_from_dragons)

    # TODO: check it actually blocks unicorn effects (for most / all unicorn
    # cards. ONLY FOR OTHER PLAYERS UNICORN CARDS!! (and ONLY unicorn cards)
