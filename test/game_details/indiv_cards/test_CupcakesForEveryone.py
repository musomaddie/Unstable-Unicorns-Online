import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class CultLeaderUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.cupcakes = find_card_in_db("Cupcakes For Everyone")
        # Remember it will enter into player[1]'s stable
        self.blow_up = find_card_in_db("Blow Up Unicorn")

    def test_enter_no_effect(self):
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        self.assertTrue(gm.PLAYERS[1].share_upgrades)
        self.assertFalse(gm.PLAYERS[0].share_upgrades)
        self.assertFalse(gm.PLAYERS[2].share_upgrades)

    def test_enter_with_card(self):
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)

        for i in range(3):
            self.assertTrue(gm.PLAYERS[i].unicorn_sacrifice_decoy,
                            "Blow up unicorn effect not set for "
                            f"player {i}.")

    def test_add_card_after_enter(self):
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)

        for i in range(3):
            self.assertTrue(gm.PLAYERS[i].unicorn_sacrifice_decoy,
                            "Blow up unicorn effect not set for "
                            f"player {i}.")

    def test_effect_card_leave(self):
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        gm._handle_leave_stable([gm.PLAYERS[1], self.blow_up, None])

        for i in range(3):
            self.assertFalse(gm.PLAYERS[i].unicorn_sacrifice_decoy,
                            "Blow up unicorn effect still set for "
                            f"player {i}.")

    # TODO: test with more upgrades: combine things

    def test_cupcakes_leave_effect_stay(self):
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        gm._handle_leave_stable([gm.PLAYERS[1], self.cupcakes, None])

        self.assertTrue(gm.PLAYERS[1].unicorn_sacrifice_decoy,
                        "Blow up unicorn not set when should be")
        self.assertFalse(gm.PLAYERS[0].unicorn_sacrifice_decoy,
                         "blow up effect still set")
        self.assertFalse(gm.PLAYERS[2].unicorn_sacrifice_decoy,
                         "Blow up effect still set")
