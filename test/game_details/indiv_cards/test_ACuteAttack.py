import copy
import os
import sys
import unittest

from unittest.mock import call

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class ACuteAttackTests(unittest.TestCase):
    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        basic_unicorn = find_card_in_db("Basic Unicorn (1)")
        self.a_cute_attack = find_card_in_db("A Cute Attack")
        for i in range(3):
            gm.PLAYERS[1].add_to_stable(copy.copy(basic_unicorn))

    def test_basic_example(self):
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=1)
        gm._handle_card_play(gm.PLAYERS[0], self.a_cute_attack)
        self.assertEqual(len(gm.PLAYERS[1].stable), 4)
        self.assertEqual(gm.PLAYERS[1].stable[0].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[1].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[2].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].stable[3].name, "Baby Unicorn")
        self.assertEqual(gm.PLAYERS[1].num_unicorns, 4)

        self.assertEqual(len(gm._make_choice.mock_calls), 4)
        self.assertEqual(gm._make_choice.mock_calls[0],
                         call(gm.PLAYERS))
        self.assertEqual(gm._make_choice.mock_calls[1],
                         call(["Baby Unicorn", "Basic Unicorn (1)",
                               "Basic Unicorn (1)", "Basic Unicorn (1)"]))
        self.assertEqual(gm._make_choice.mock_calls[2],
                         call(["Baby Unicorn", "Basic Unicorn (1)",
                               "Basic Unicorn (1)", "Baby Unicorn"]))
        self.assertEqual(gm._make_choice.mock_calls[3],
                         call(["Baby Unicorn", "Basic Unicorn (1)",
                               "Baby Unicorn", "Baby Unicorn"]))
