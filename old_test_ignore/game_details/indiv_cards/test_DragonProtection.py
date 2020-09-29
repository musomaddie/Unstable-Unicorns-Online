import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class DragonProtectionTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Dragon Protection"))

    def test_enter_effect(self):
        self.assertTrue(gm.PLAYERS[0].protected_from_unicorn)
        self.assertEqual(len(gm._make_choice.mock_calls), 1)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS))

    def test_leave_effect(self):
        gm._handle_leave_stable([gm.PLAYERS[0],
                                 find_card_in_db("Dragon Protection"),
                                 None])
        self.assertFalse(gm.PLAYERS[0].protected_from_unicorn)

    # TODO: check it actually blocks unicorn effects (for most / all unicorn
    # cards. ONLY FOR OTHER PLAYERS UNICORN CARDS!! (and ONLY unicorn cards)
