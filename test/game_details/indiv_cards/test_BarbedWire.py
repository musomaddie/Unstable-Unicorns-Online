import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
import game_details.game_manager as gm


class BarbedWireTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.barbed_wire = find_card_in_db("Barbed Wire")
        self.basic = find_card_in_db("Apprentice Unicorn")
        gm._add_to_stable([gm.PLAYERS[0], self.barbed_wire, None])

    def test_basic(self):

        # Confirm everything is as expected here
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(gm.PLAYERS[0].hand), 5)
        self.assertEqual(len(gm.DISCARD_PILE), 0)

        # First test what happens when a unicorn is played
        gm._handle_card_play(gm.PLAYERS[0], self.basic)

        self.assertEqual(len(gm.PLAYERS[0].stable), 3)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(gm.PLAYERS[0].hand), 4)
        self.assertEqual(len(gm.DISCARD_PILE), 1)

        # Test what happens when unicorn is removed
        gm._handle_leave_stable([gm.PLAYERS[0], self.basic, None])
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)
        self.assertEqual(len(gm.DISCARD_PILE), 3)

        # Then remove barbed wire (will not discard in addition)
        gm._handle_leave_stable([gm.PLAYERS[0], self.barbed_wire, None])
        self.assertEqual(len(gm.PLAYERS[0].stable), 1)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 1)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)
        self.assertEqual(len(gm.DISCARD_PILE), 4)
        self.assertTrue(self.barbed_wire in gm.DISCARD_PILE)

        # Play unicorn again
        gm._handle_card_play(gm.PLAYERS[0], self.basic)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(gm.PLAYERS[0].hand), 3)