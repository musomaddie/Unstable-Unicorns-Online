import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.PlayerManager import PlayerManager
from game_details.NurseryManager import NurseryManager
from tests.game_details.setup import find_card_in_db


CARD_UNICORN_NAME = "Angel Unicorn"

@pytest.fixture
def player_manager():
    return PlayerManager("Alice")

@pytest.fixture
def example_card():
    return find_card_in_db(CARD_UNICORN_NAME)

def test_add_baby(player_manager):
    nursery = NurseryManager()
    original_size = len(nursery.cards)
    player_manager.add_baby(nursery)

    assert player_manager.player.stable.size() == 1
    assert len(nursery.cards) == original_size - 1

def test_add_to_hand(player_manager, example_card):
    player_manager.add_to_hand(example_card)
    assert len(player_manager.player.hand.cards) == 1
    assert player_manager.player.hand.cards[0].name_equals(
            CARD_UNICORN_NAME)

def test_add_to_stable(player_manager, example_card):
    player_manager.add_to_stable(example_card)
    assert player_manager.player.stable.size() == 1
    assert player_manager.player.stable.unicorns[0].name_equals(CARD_UNICORN_NAME)

def test_has_won_false(player_manager):
    assert not player_manager.has_won()

def test_has_won_true(player_manager, example_card):
    [player_manager.add_to_stable(example_card) for _ in range(7)]
    assert player_manager.has_won()
