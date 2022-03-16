import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.NurseryManager import NurseryManager
from game_details.PlayersManager import PlayersManager
from tests.game_details.setup import random_selection_from_db

CARD_UNICORN_NAME = "Angel Unicorn"

@pytest.fixture
def players_manager():
    return PlayersManager(["Alice", "Bob"])

def test_prepare_game_start(players_manager):
    nursery = NurseryManager()
    original_nursery_size = len(nursery.cards)
    original_deck_size = 20

    deck = random_selection_from_db(original_deck_size)
    players_manager.prepare_game_start(nursery, deck)

    # Check deck size
    assert len(players_manager.players[0].player.hand.cards) == 5
    assert len(players_manager.players[1].player.hand.cards) == 5
    assert len(deck.cards) == original_deck_size - 10

    # Check nursery
    assert players_manager.players[0].player.stable.size() == 1
    assert players_manager.players[1].player.stable.size() == 1
    assert len(nursery.cards) == original_nursery_size - 2

def test_all_players(players_manager):
    all_players = players_manager.all_players()
    assert len(all_players) == 2
    assert all_players[0].player.name == "Alice"
    assert all_players[1].player.name == "Bob"

def test_find_player_from_index(players_manager):
    assert players_manager.find_player_from_index(0).player.name == "Alice"
