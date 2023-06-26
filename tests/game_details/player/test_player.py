from io import StringIO

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType
from game_details.discard_pile import DiscardPile
from game_details.hand import Hand
from game_details.player import Player
from game_details.utilities import ActionType
from tests.conftest import create_deck_with_special_first_card


@pytest.fixture
def player() -> Player:
    return Player("Alice")


def test_draw_card(player, fake_card):
    testing_card = Card("Testing First", CardType.BASIC_UNICORN, "Text")
    deck = create_deck_with_special_first_card(testing_card, fake_card)
    deck_size_before = len(deck)
    hand_size_before = len(player.hand)

    player.draw_card(deck)

    assert len(deck) == deck_size_before - 1
    assert len(player.hand) == hand_size_before + 1
    assert testing_card in player.hand


def test_choose_play_card_or_draw(player):
    assert player.choose_play_card_or_draw() == ActionType.DRAW_CARD


class TestDiscardToHandLimit:

    @fixture
    def discard_pile(self):
        return DiscardPile()

    def test_no_cards(self, player, discard_pile):
        assert len(player.hand) == 0
        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 0
        assert len(discard_pile) == 0

    def test_not_enough_for_hand_limit(self, player, discard_pile, monkeypatch):
        player.hand = Hand([Card("C1", CardType.BASIC_UNICORN, ""), Card("C2", CardType.BASIC_UNICORN, "")])
        monkeypatch.setattr("sys.stdin", StringIO("0"))

        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 2
        assert len(discard_pile) == 0

    def test_one_over_default_hand_limit(self, player, discard_pile, monkeypatch):
        player.hand = Hand(
            [Card(f"C{i}", CardType.MAGIC, "") for i in range(8)]
        )
        monkeypatch.setattr("sys.stdin", StringIO("0"))

        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 7
        assert len(discard_pile) == 1
        assert discard_pile[0].name == "C0"

    def test_three_over_default_hand_limit(self, player, discard_pile, monkeypatch):
        # TODO - suppress output.
        player.hand = Hand(
            [Card(f"C{i}", CardType.BASIC_UNICORN, "") for i in range(10)]
        )
        monkeypatch.setattr("sys.stdin", StringIO("0\n0\n0"))

        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 7
        assert len(discard_pile) == 3
        assert discard_pile[0].name == "C2"
        assert discard_pile[1].name == "C1"
        assert discard_pile[2].name == "C0"
