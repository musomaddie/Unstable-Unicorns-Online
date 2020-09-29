import copy
import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
from game_details.CardLocation import CardLocation
import game_details.game_manager as gm


class AngryDragoncornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.angry_dragoncorn = find_card_in_db("Angry Dragoncorn")

        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        self.orig_hands = [copy.copy(player.hand) for player in gm.PLAYERS]
        gm._handle_card_play(gm.PLAYERS[0], self.angry_dragoncorn)

    def test_basic_example(self):
        self.assertEqual(len(gm.DISCARD_PILE), 3)
        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].stable[1].name, "Angry Dragoncorn")
        self.assertEqual(self.angry_dragoncorn.location,
                         CardLocation.STABLE)

        for player in gm.PLAYERS:
            self.assertEqual(len(player.hand), 4)

        self.assertEqual(len(gm._make_choice.mock_calls), 3)
        for i in range(len(gm.PLAYERS)):
            self.assertEqual(gm._make_choice.mock_calls[i],
                             call(self.orig_hands[i]))
