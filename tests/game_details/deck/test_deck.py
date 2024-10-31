""" tests for deck """
import copy

from tests.conftest import create_deck_with_special_first_card
from unstable_unicorns_game.game_details.card import CardType
from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.deck import Deck


def test_constructor(fake_card):
    deck = Deck([copy.copy(fake_card) for _ in range(3)])
    assert len(deck) == 3
    assert deck[0] == fake_card


def test_draw_top(fake_card):
    special_card = card_factory.create_default("Special", CardType.BASIC_UNICORN)
    card_stack = create_deck_with_special_first_card(special_card, fake_card)
    size_before = len(card_stack)

    result_card = card_stack.draw_top()

    assert result_card == special_card
    assert len(card_stack) == size_before - 1
