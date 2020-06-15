import unittest
import os
import sys
import sqlite3

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from game_details.game_manager import create_game
from game_details.game_manager import DECK as deck

NUM_CARDS_STANDARD = 111
NUM_CARDS_RAINBOW = 44
NUM_CARDS_NSFW = 42
NUM_CARDS_UNCUT = 41
NUM_CARDS_DRAGON = 49


class StartingDeck(unittest.TestCase):

    def test_all_decks(self):
        create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"])
        self.assertEqual(len(deck),
                         NUM_CARDS_STANDARD + NUM_CARDS_RAINBOW
                         + NUM_CARDS_NSFW + NUM_CARDS_UNCUT
                         + NUM_CARDS_DRAGON)

    def test_nsfw_decks(self):
        create_game(["Uncut", "NSFW"])
        self.assertEqual(len(deck),
                         NUM_CARDS_NSFW + NUM_CARDS_UNCUT)

    def test_one_deck_not_standard(self):
        create_game(["Dragon"])
        self.assertEqual(len(deck), 0)

    def test_only_standard(self):
        create_game(["Standard"])
        self.assertEqual(len(deck), NUM_CARDS_STANDARD)

    def test_nonexistent_deck(self):
        create_game(["FOO"])
        self.assertEqual(len(deck), 0)

    def test_no_deck(self):
        create_game([])
        self.assertEqual(len(deck), 0)

    def test_nonexistent_deck_with_existent(self):
        create_game(["FOO", "Standard"])
        self.assertEqual(len(deck), NUM_CARDS_STANDARD)


if __name__ == '__main__':
    unittest.main()
