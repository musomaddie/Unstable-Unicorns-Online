import copy

import pytest

from game_details.card import Card, CardType
from game_details.deck import Deck
from game_details.hand import Hand
from game_details.player import Player
from game_details.stable import Stable


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


def create_default_player(name: str):
    return Player(name, Hand(), Stable.create_stable(
        Card("Babyyyy", CardType.BABY_UNICORN, "I'm just a baby")))


def create_deck_with_special_first_card(first_card: Card, other_card: Card) -> Deck:
    deck = Deck()
    deck.cards.append(first_card)
    for _ in range(10):
        deck.cards.append(copy.copy(other_card))
    return deck
