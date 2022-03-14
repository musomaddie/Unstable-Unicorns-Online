import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.HandManager import HandManager
from game_details.Player import Player
from tests.game_details.setup import find_card_in_db

CARD_1_NAME = "A Cute Attack"
CARD_2_NAME = "Angel Unicorn"

@pytest.fixture
def example_card():
    return find_card_in_db(CARD_1_NAME)

@pytest.fixture
def existing_hand():
    return [find_card_in_db(CARD_2_NAME)]

def test_add_card(example_card, existing_hand):
    hand_manager = HandManager(Player("Alice"))
    hand_manager.cards = existing_hand

    hand_manager.add_card(example_card)

    assert len(hand_manager.cards) == 2
    assert hand_manager.cards[0].name_equals(CARD_2_NAME)
    assert hand_manager.cards[1].name_equals(CARD_1_NAME)
