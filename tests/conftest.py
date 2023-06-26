import copy

import pytest

from game_details.card import Card, CardType, CardStack
from game_details.deck import Deck


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


def create_deck_with_special_first_card(first_card: Card, other_card: Card) -> CardStack:
    deck = Deck()
    deck.cards.append(first_card)
    for _ in range(10):
        deck.cards.append(copy.copy(other_card))
    return deck
