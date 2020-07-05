import os
import sys
import unittest

from unittest.mock import MagicMock

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BlowUpUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.blow_up = find_card_in_db("Blow Up Unicorn")

    def test_add_condition(self):
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2,
                         "Blow Up Unicorn not added to stable")
        self.assertTrue(self.blow_up in gm.PLAYERS[0].stable,
                        "Stable does not contain the blow up unicorn")
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1,
                         "Blow Up Unicorn counted as unicorn (not upgrade)")
        self.assertTrue(gm.PLAYERS[0].unicorn_sacrifice_decoy,
                        "Sacrifice decoy not set to true")
        self.assertTrue(gm.PLAYERS[0].unicorn_destroy_decoy,
                        "Destroy decoy not set to true")

        # Assert mock
        gm._make_choice.assert_called_once_with(gm.PLAYERS)

    def test_leave_condition(self):
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        gm._handle_leave_stable([gm.PLAYERS[0], self.blow_up, None])

        self.assertEqual(len(gm.PLAYERS[0].stable), 1,
                         "Blow up unicorn has not left stable")
        self.assertFalse(gm.PLAYERS[0].unicorn_sacrifice_decoy,
                         "Sacrifice decoy not reset to false")
        self.assertFalse(gm.PLAYERS[0].unicorn_destroy_decoy,
                         "Destroy decoy not reset to false")

    def test_activates_on_sacrifice(self):
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.blow_up)
        gm._handle_sacrifice_this_card([gm.PLAYERS[0],
                                        gm.PLAYERS[0].stable[0],
                                        None])

        # Assert correct card remains in stable
        self.assertEqual(len(gm.PLAYERS[1].stable), 1,
                         "Nothing left the stable")
        self.assertEqual(gm.PLAYERS[1].num_unicorns, 1,
                         "The number of unicorns remaining is wrong")
        self.assertEqual(gm.PLAYERS[1].stable[0].name,
                         "Baby Unicorn",
                         "The card in the stable is not the unicorn")
        self.assertTrue(self.blow_up in gm.DISCARD_PILE,
                        "The discard pile does not contain the blow up "
                        "unicorn")

        # Assert the decoy values updated correctly
        self.assertFalse(gm.PLAYERS[1].unicorn_sacrifice_decoy,
                         "Sacrifice decoy not reset to false")
        self.assertFalse(gm.PLAYERS[1].unicorn_destroy_decoy,
                         "Destroy decoy not reset to false")

    # TODO: test works on destroy
