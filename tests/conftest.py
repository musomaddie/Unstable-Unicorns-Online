import copy

import pytest

from game_details.card import Card, CardType, CardPile


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


def create_card_stack_with_special_first_card(first_card: Card, other_card: Card) -> CardPile:
    card_pile = CardPile()
    card_pile.cards.append(first_card)
    for _ in range(10):
        card_pile.cards.append(copy.copy(fake_card))
    return card_pile
