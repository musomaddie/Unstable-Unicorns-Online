import copy

import pytest

from game_details.card.card import Card
from game_details.card.card_type import CardType
from game_details.deck.deck_manager import Deck
from game_details.discard_pile.discard_pile_manager import DiscardPile
from game_details.nursery.nursery import Nursery
from game_details.player.all_players_manager import AllPlayers
from game_details.player.player import Player
from game_details.turn.turn import Turn


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


def test_create_turn(fake_card):
    players = [Player("Alice"), Player("Bob"), Player("Charlie")]
    example_turn = Turn(
        Deck([copy.copy(fake_card)]),
        DiscardPile([copy.copy(fake_card)]),
        Nursery([copy.copy(fake_card)]),
        players[0],
        AllPlayers(players)
    )
    print(example_turn)
