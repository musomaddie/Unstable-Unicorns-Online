import os
import sys
import unittest


sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class BearDaddyUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        self.bear_daddy = find_card_in_db("Bear Daddy Unicorn")

    def test_basic(self):
        original_deck_size = len(gm.DECK)
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        gm._handle_card_play(gm.PLAYERS[0], self.bear_daddy)

        self.assertEqual(len(gm.PLAYERS[0].stable), 2)
        self.assertEqual(gm.PLAYERS[0].num_unicorns, 2)
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "Twinkicorn was not added to hand")
        self.assertEqual(len(gm.DECK), original_deck_size - 1,
                         "Twinkicorn was not removed from deck")

        gm._make_choice.assert_called_once()
        call_args = gm._make_choice.call_args
        args, kwargs = call_args
        for item in args[0]:
            self.assertEqual("Twinkicorn", item)
