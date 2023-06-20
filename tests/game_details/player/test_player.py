import pytest

from game_details.card import Card, CardType
from game_details.player import Player
from game_details.utilities import ActionType
from tests.conftest import create_card_stack_with_special_first_card


@pytest.fixture
def player() -> Player:
    return Player("Alice")


def test_draw_card(player, fake_card):
    testing_card = Card("Testing First", CardType.BASIC_UNICORN, "Text")
    deck = create_card_stack_with_special_first_card(testing_card, fake_card)
    deck_size_before = len(deck)
    hand_size_before = len(player.hand)

    player.draw_card(deck)

    assert len(deck) == deck_size_before - 1
    assert len(player.hand) == hand_size_before + 1
    assert testing_card in player.hand


def test_choose_play_card_or_draw(player):
    assert player.choose_play_card_or_draw() == ActionType.DRAW_CARD
