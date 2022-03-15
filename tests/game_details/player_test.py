import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.Player import Player
from tests.game_details.setup import find_card_in_db


CARD_UNICORN_NAME = "Angel Unicorn"

@pytest.fixture
def example_player():
    return Player("Alice")

@pytest.fixture
def example_card():
    return find_card_in_db(CARD_UNICORN_NAME)

def test_player_setup(example_player):
    assert example_player.name == "Alice"
    assert len(example_player.hand.cards) == 0
    assert example_player.stable.size() == 0

def test_add_to_stable(example_player, example_card):
    example_player.add_to_stable(example_card)
    assert example_player.stable.size() == 1

def test_add_to_hand(example_player, example_card):
    example_player.add_to_hand(example_card)
    assert len(example_player.hand.cards) == 1
