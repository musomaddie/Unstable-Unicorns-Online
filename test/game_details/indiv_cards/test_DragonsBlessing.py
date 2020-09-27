import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db, MagicMock
import game_details.game_manager as gm


class DragonsBlessingTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        self.dragons_blessing = find_card_in_db("Dragon's Blessing")
        self.downgrade = find_card_in_db("Barbed Wire")
        self.cupcakes = find_card_in_db("Cupcakes For Everyone")
        self.upgrade = find_card_in_db("Dragon Protection")
        # Handling card play added to each specific tests to allow for
        # downgrade cards to be added before the card is played

    def test_basic_example(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)

        self.assertTrue("Dragon's Blessing" in gm.PLAYERS[0].stable,
                        "Dragon's Blessing not added to stable")
        self.assertTrue(gm.PLAYERS[0].downgrades_have_no_effect,
                        "The toggle option is not set")
        self.assertTrue("Dragon's Blessing" in gm.PLAYERS[0].stable)
        # Mock used once to select the player
        self.assertEqual(len(gm._make_choice.mock_calls), 1)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS))

    def test_basic_leave(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_leave_stable([gm.PLAYERS[0], self.dragons_blessing, None])
        self.assertFalse(gm.PLAYERS[0].downgrades_have_no_effect)
        self.assertFalse("Dragon's Blessing" in gm.PLAYERS[0].stable)

    def test_basic_existing_downgrade(self):
        gm._handle_card_play(gm.PLAYERS[0], self.downgrade)
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        self.assertFalse(gm.PLAYERS[0].barbed_wire_effect)

    def test_basic_adding_downgrade(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_card_play(gm.PLAYERS[0], self.downgrade)
        self.assertFalse(gm.PLAYERS[0].barbed_wire_effect)

    def test_basic_downgrade_remove(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_card_play(gm.PLAYERS[0], self.downgrade)
        gm._handle_leave_stable([gm.PLAYERS[0], self.dragons_blessing, None])
        self.assertTrue(gm.PLAYERS[0].barbed_wire_effect,
                        "Downgrade not turned back after removing protection")

    def test_downgrade_removed_first(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_card_play(gm.PLAYERS[0], self.downgrade)
        gm._handle_leave_stable([gm.PLAYERS[0], self.downgrade, None])

        self.assertFalse(gm.PLAYERS[0].barbed_wire_effect,
                         "The downgrade effect is active after leaving")
        self.assertTrue(gm.PLAYERS[0].downgrades_have_no_effect)

    def test_cupcakes_existing_turn_off(self):
        print("RUNNING FAILING TEST!!!!!!!!!!!!!!!!")
        # Ensures that the cupcake effect is handled correctly when these two
        # cards collide
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        gm._handle_card_play(gm.PLAYERS[0], self.upgrade)
        gm._handle_card_play(gm.PLAYERS[0],  self.dragons_blessing)

        self.assertTrue(gm.PLAYERS[0].downgrades_have_no_effect)
        self.assertFalse(gm.PLAYERS[0].share_upgrades,
                         "Cupcakes downgrade not toggled off")
        self.assertTrue(gm.PLAYERS[0].protected_from_unicorn,
                        "Upgrade toggled off")
        for i in range(1, 3):
            self.assertFalse(gm.PLAYERS[i].protected_from_unicorn,
                             "Upgrade still set")
            self.assertFalse(gm.PLAYERS[i].downgrades_have_no_effect,
                             f"New upgrade set for {i}")

    def test_cupcakes_play_turn_off(self):
        # Ensures that the cupcake effect is handled correctly when these two
        # cards collide
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_card_play(gm.PLAYERS[0], self.upgrade)
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)

        self.assertFalse(gm.PLAYERS[0].share_upgrades,
                         "Cupcakes downgrade was not toggled off")
        self.assertTrue(gm.PLAYERS[0].protected_from_unicorn,
                       "Upgrade toggled off for the current player")
        for i in range(1, 3):
            self.assertFalse(gm.PLAYERS[i].protected_from_unicorn,
                             "Upgrade still set for another player")
            self.assertFalse(gm.PLAYERS[i].downgrades_have_no_effect,
                             "New upgrade set for different player")

    def test_cupcakes_turn_back_on(self):
        gm._handle_card_play(gm.PLAYERS[0], self.dragons_blessing)
        gm._handle_card_play(gm.PLAYERS[0], self.upgrade)
        gm._handle_card_play(gm.PLAYERS[0], self.cupcakes)
        gm._handle_leave_stable([gm.PLAYERS[0], self.dragons_blessing, None])

        self.assertTrue(gm.PLAYERS[0].share_upgrades,
                        "Cupcakes downgrade was not reactivated")
        for i in range(3):
            self.assertTrue(gm.PLAYERS[i].protected_from_unicorn,
                            f"The upgrade was not returned to player {i}")

    # TODO: ensure it still works correctly when any downgrade leaves the
    # stable while this is still active
