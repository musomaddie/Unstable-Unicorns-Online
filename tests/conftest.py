import copy

import pytest

from game_details.card import Card, CardType, CardStack


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")


def create_card_stack_with_special_first_card(first_card: Card, other_card: Card) -> CardStack:
    card_stack = CardStack()
    card_stack.cards.append(first_card)
    for _ in range(10):
        card_stack.cards.append(copy.copy(other_card))
    return card_stack
