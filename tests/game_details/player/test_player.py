""" tests for discard pile. """
from io import StringIO

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType
from game_details.discard_pile import DiscardPile
from game_details.hand import Hand
from game_details.player import Player
from game_details.utilities import TurnActionType
from play_deciders import QueueDecider
from tests.conftest import create_deck_with_special_first_card, create_default_player


@pytest.fixture
def player() -> Player:
    """ Returns a player for testing. """
    return create_default_player("Alice")


def test_init_default(player):
    assert player.name == "Alice"
    assert len(player.hand) == 0
    assert len(player.stable.unicorns) == 1
    assert player.stable.unicorns[0].card_type == CardType.BABY_UNICORN


def test_draw_card(player, fake_card):
    testing_card = Card.create_default("Testing First", CardType.BASIC_UNICORN)
    deck = create_deck_with_special_first_card(testing_card, fake_card)
    deck_size_before = len(deck)
    hand_size_before = len(player.hand)

    player.draw_card(deck)

    assert len(deck) == deck_size_before - 1
    assert len(player.hand) == hand_size_before + 1
    assert testing_card in player.hand


def test_choose_play_card_or_draw(player):
    assert player.choose_play_card_or_draw() == TurnActionType.DRAW_CARD


# noinspection PyStatementEffect
# suppressed for capsys statements which in turn suppress additional print I don't want to see in the test output.
class TestDiscardToHandLimit:

    @fixture
    def discard_pile(self):
        """ Discard pile"""
        return DiscardPile.create_default()

    def test_no_cards(self, player, discard_pile):
        assert len(player.hand) == 0
        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 0
        assert len(discard_pile) == 0

    def test_not_enough_for_hand_limit(self, player, discard_pile, monkeypatch):
        player.hand = Hand(
            [Card.create_default("C1", CardType.BASIC_UNICORN), Card.create_default("C2", CardType.BASIC_UNICORN)])
        monkeypatch.setattr("sys.stdin", StringIO("0"))

        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 2
        assert len(discard_pile) == 0

    def test_one_over_default_hand_limit(self, player, discard_pile, monkeypatch, capsys):
        player.hand = Hand(
            [Card.create_default(f"C{i}", CardType.MAGIC) for i in range(8)]
        )
        player.hand.connect_play_decider(QueueDecider(player))
        monkeypatch.setattr("sys.stdin", StringIO("1"))

        player.discard_to_hand_limit(discard_pile)

        capsys.readouterr().out

        assert len(player.hand) == 7
        assert len(discard_pile) == 1
        assert discard_pile[0].name == "C0"

    def test_three_over_default_hand_limit(self, player, discard_pile, monkeypatch, capsys):
        player.hand = Hand(
            [Card.create_default(f"C{i}", CardType.BASIC_UNICORN) for i in range(10)]
        )
        player.hand.connect_play_decider(QueueDecider(player))
        monkeypatch.setattr("sys.stdin", StringIO("1\n1\n1"))

        player.discard_to_hand_limit(discard_pile)
        capsys.readouterr().out

        assert len(player.hand) == 7
        assert len(discard_pile) == 3
        assert discard_pile[0].name == "C2"
        assert discard_pile[1].name == "C1"
        assert discard_pile[2].name == "C0"
