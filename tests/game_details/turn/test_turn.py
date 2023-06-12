import copy

import pytest

from game_details.card import Card, CardType
from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.nursery import Nursery
from game_details.player import Player, AllPlayers
from game_details.turn import Turn


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


class TestTurnParts:
    @pytest.fixture
    def deck(self) -> Deck:
        return Deck([copy.copy(fake_card) for _ in range(5)])

    @pytest.fixture
    def discard_pile(self) -> DiscardPile:
        return DiscardPile()

    @pytest.fixture
    def nursery(self) -> Nursery:
        return Nursery()

    @pytest.fixture
    def players(self) -> list[Player]:
        return [Player("Alice"), Player("Bob"), Player("Charlie")]

    @pytest.fixture
    def turn(self, deck, discard_pile, nursery, players):
        return Turn(deck, discard_pile, nursery, players[0], AllPlayers(players))

    def test_take_turn(self, turn):
        turn.take_turn()
