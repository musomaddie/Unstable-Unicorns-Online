import os
import sys
import unittest

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

from test.game_details.setup import find_card_in_db, MagicMock
import game_details.game_manager as gm


class DragonTamerUnicornTests(unittest.TestCase):

    def setUp(self):
        gm.create_game(["Standard", "Dragon", "Rainbow", "Uncut", "NSFW"],
                       ["Alice", "Bob", "Charlie"])
        gm._make_choice = MagicMock(name="Make Choice",
                                    return_value=0)
        gm._handle_card_play(gm.PLAYERS[0],
                             find_card_in_db("Dragon Tamer Unicorn"))

    def test_basic_example(self):
        self.assertTrue("Dragon Tamer Unicorn" in gm.PLAYERS[0].stable,
                        "Dragon Tamer Unicorn not added to stable")
        self.assertEqual(len(gm.PLAYERS[0].hand), 6,
                         "Dragon card not added to hand")
        self.assertTrue("Dragon" in gm.PLAYERS[0].hand[5].name,
                        "The drawn card is not a dragon card")

        # assert the mock
        gm._make_choice.assert_called_once()
        call_args = gm._make_choice.call_args
        args, kwargs = call_args
        for item in args[0]:
            self.assertTrue("Dragon" in item.name,
                            "A hard being searched does not match the search "
                            "condition")
