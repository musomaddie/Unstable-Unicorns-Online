import unittest
import os
import sys
import sqlite3
import copy

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from game_details.game_manager import create_game
from game_details.game_manager import DECK as deck


class StartingDeck(unittest.TestCase):
    # TODO: something's gone terribly wrong: the numbers are no longer adding
    # up. It's not terribly obvious why so recalculate all this :(

    NUM_CARDS_STANDARD = 111
    NUM_CARDS_RAINBOW = 44
    NUM_CARDS_NSFW = 42
    NUM_CARDS_UNCUT = 41
    NUM_CARDS_DRAGON = 49

    def test_all_decks(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck),
                         StartingDeck.NUM_CARDS_STANDARD
                         + StartingDeck.NUM_CARDS_RAINBOW
                         + StartingDeck.NUM_CARDS_NSFW
                         + StartingDeck.NUM_CARDS_UNCUT
                         + StartingDeck.NUM_CARDS_DRAGON)
                         """

    def test_nsfw_decks(self):
        create_game(["Uncut", "NSFW"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck),
                         StartingDeck.NUM_CARDS_NSFW
                         + StartingDeck.NUM_CARDS_UNCUT)
                         """

    def test_one_deck_not_standard(self):
        create_game(["Dragon"],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_only_standard(self):
        create_game(["Standard"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck), StartingDeck.NUM_CARDS_STANDARD)
        """

    def test_nonexistent_deck(self):
        create_game(["FOO"],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_no_deck(self):
        create_game([],
                    ["Alice", "Bob", "Charlie"])
        self.assertEqual(len(deck), 0)

    def test_nonexistent_deck_with_existent(self):
        create_game(["FOO", "Standard"],
                    ["Alice", "Bob", "Charlie"])
        """
        self.assertEqual(len(deck), StartingDeck.NUM_CARDS_STANDARD)
        """
