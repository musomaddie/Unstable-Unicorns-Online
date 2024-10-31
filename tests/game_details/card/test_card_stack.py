""" Tests for card. """
from tests.conftest import create_deck_with_special_first_card
from unstable_unicorns_game.game_details.card import CardType, CardStack
from unstable_unicorns_game.game_details.card.factory import card_factory


def test_add_top(fake_card):
    card_stack = CardStack.create_default()
    size_before = len(card_stack)

    card_stack.add_top(fake_card)

    assert len(card_stack) == size_before + 1
    assert card_stack[0] == fake_card

    second_card = card_factory.create_default("Second added card", CardType.BASIC_UNICORN)

    card_stack.add_top(second_card)

    assert len(card_stack) == size_before + 2
    assert card_stack[0].name == "Second added card"


def test_pop_top(fake_card):
    special_card = card_factory.create_default("Special", CardType.BASIC_UNICORN)
    card_stack = create_deck_with_special_first_card(special_card, fake_card)
    size_before = len(card_stack)

    result_card = card_stack.pop_top()

    assert result_card == special_card
    assert len(card_stack) == size_before - 1
