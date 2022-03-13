import os
import sys
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import CopyingMock, find_card_in_db
import game_details.game_manager as gm


class DragonKissTests(unittest.TestCase):

    def setUp(self):
        gm._make_choice = CopyingMock(name="Make Choice",
                                      return_value=0)
        gm.PLAYERS[0].add_to_hand(find_card_in_db("Dragon Kiss"))
        gm._handle_card_play(gm.PLAYERS[0], find_card_in_db("Dragon Kiss"))

    def test_basic_example(self):
        self.assertTrue(len(gm.DISCARD_PILE) >= 2,
                        "Both magic cards have not been added to the discard "
                        "pile")
        self.assertEqual(gm.DISCARD_PILE[1].card_type, "Magic")

        # assert the mock
        call_args = gm._make_choice.call_args
        args, kwargs = call_args
        for item in args[0]:
            self.assertEqual("Magic", item.card_type)  # TODO: this fails occasionally. Why?
