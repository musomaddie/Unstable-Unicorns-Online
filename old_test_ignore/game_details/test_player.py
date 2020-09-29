import unittest
import sys
import os

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db
from game_details.Player import Player


class PlayerTests(unittest.TestCase):

    def setUp(self):
        self.player = Player("Alice", find_card_in_db("Baby Unicorn"))

    def test_basic_setUp(self):
        self.assertEqual(self.player.name, "Alice",
                         "Name is not set up correctly")
        self.assertEqual(self.player.hand, [],
                         "The hand is not set up correctly")
        self.assertEqual(len(self.player.stable), 1,
                         "The stable has the wrong number of unicorns")
        self.assertEqual(self.player.stable[0], "Baby Unicorn",
                         "The unicorn in the stable is not a baby")
        self.assertEqual(self.player.num_unicorns, 1,
                         "The stable has the wrong number of unicorns (num)")

    def test_get_stable_modifiers(self):
        # Try with 0
        self.assertEqual(self.player.get_stable_modifiers(), [],
                         "Did not work correctly on an empty list")

        # Try with 1
        self.player.add_to_stable(find_card_in_db("Barbed Wire"))
        self.assertEqual(len(self.player.get_stable_modifiers()), 1,
                         "Did not find the correct number of items "
                         "when the list contained one")
        self.assertTrue("Barbed Wire" in self.player.get_stable_modifiers(),
                        "The card is missing from the result")

        # Test with 2
        self.player.add_to_stable(find_card_in_db("Blow Up Unicorn"))
        self.assertEqual(len(self.player.get_stable_modifiers()), 2,
                         "Did not find the correct number of items")
        self.assertTrue("Barbed Wire" in self.player.get_stable_modifiers(),
                        "The first added card is missing (downgrade)")
        self.assertTrue("Blow Up Unicorn" in
                        self.player.get_stable_modifiers(),
                        "The newly added card is missing (upgrade)")

        # Test with an additional basic unicorn
        self.player.add_to_stable(find_card_in_db("Basic Unicorn (3)"))
        self.assertEqual(len(self.player.get_stable_modifiers()), 2,
                         "The unicorn has been returned :( ")
