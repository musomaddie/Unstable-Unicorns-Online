""" tests for discard pile. """
from io import StringIO

import pytest

from game_details.card import CardType
from game_details.card.factory import card_factory
from game_details.hand.factory import hand_factory
from game_details.hand.impl.hand_impl import HandImpl
from game_details.player import Player
from game_details.utilities import TurnActionType
from tests.conftest import create_deck_with_special_first_card, create_default_player


@pytest.fixture
def player() -> Player:
    """ Returns a player for testing. """
    return create_default_player("Aelin")


def test_init_default(player):
    assert player.name == "Aelin"
    assert len(player.hand) == 0
    assert len(player.stable.unicorns) == 1
    assert player.stable.unicorns[0].card_type == CardType.BABY_UNICORN


def test_draw_card(player, fake_card):
    testing_card = card_factory.create_default("Testing First", CardType.BASIC_UNICORN)
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

    def test_no_cards(self, player, discard_pile):
        assert len(player.hand) == 0
        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 0
        assert len(discard_pile) == 0

    def test_not_enough_for_hand_limit(self, player, discard_pile, monkeypatch):
        player.hand = HandImpl(cards=[
            card_factory.create_default("C1", CardType.BASIC_UNICORN),
            card_factory.create_default("C2", CardType.BASIC_UNICORN)])
        monkeypatch.setattr("sys.stdin", StringIO("0"))

        player.discard_to_hand_limit(discard_pile)

        assert len(player.hand) == 2
        assert len(discard_pile) == 0

    def test_one_over_default_hand_limit(self, player, discard_pile, monkeypatch, capsys):
        player.hand = hand_factory.create_only_cards(
            [card_factory.create_default(f"C{i}", CardType.MAGIC) for i in range(8)]
        )
        monkeypatch.setattr("sys.stdin", StringIO("1"))

        player.discard_to_hand_limit(discard_pile)

        capsys.readouterr().out

        assert len(player.hand) == 7
        assert len(discard_pile) == 1
        assert discard_pile[0].name == "C0"

    def test_three_over_default_hand_limit(self, player, discard_pile, monkeypatch, capsys):
        player.hand = hand_factory.create_only_cards(
            [card_factory.create_default(f"C{i}", CardType.BASIC_UNICORN) for i in range(10)])
        monkeypatch.setattr("sys.stdin", StringIO("1\n1\n1"))

        player.discard_to_hand_limit(discard_pile)
        capsys.readouterr().out

        assert len(player.hand) == 7
        assert len(discard_pile) == 3
        assert discard_pile[0].name == "C2"
        assert discard_pile[1].name == "C1"
        assert discard_pile[2].name == "C0"


class TestTakeTurn:
    def test_turn_draws_card(self, player, fake_deck, discard_pile):
        """ Asserts that a card is drawn at the start of the turn. """
        starting_hand_size = len(player.hand)
        starting_deck_size = len(fake_deck)

        top_deck_card = fake_deck[0]

        player.take_turn(fake_deck, discard_pile)

        # + 2 because the default turn action is to draw again.
        assert len(player.hand) == starting_hand_size + 2
        assert len(fake_deck) == starting_deck_size - 2
        assert player.hand[0] == top_deck_card

    def test_action_phase_draw(self, player, fake_deck, discard_pile):
        """ Asserts that a card is drawn as part of the draw action phase. """
        starting_hand_size = len(player.hand)
        starting_deck_size = len(fake_deck)

        second_deck_card = fake_deck[1]

        player.take_turn(fake_deck, discard_pile)

        # +2 since the draw phase also draws a card.
        assert len(player.hand) == starting_hand_size + 2
        assert len(fake_deck) == starting_deck_size - 2
        assert player.hand[1] == second_deck_card

    @pytest.mark.parametrize(
        ("hand_size_sot", "expected_discard_size", "expected_hand_size_eot"),
        [(1, 0, 3), (7, 2, 7), (10, 5, 7), (8, 3, 7)]
    )
    def test_discard_to_hand_limit(
            self, hand_size_sot, expected_discard_size, expected_hand_size_eot, discard_pile, fake_deck, player):
        starting_discard_size = len(discard_pile)
        [player.draw_card(fake_deck) for _ in range(hand_size_sot)]

        player.take_turn(fake_deck, discard_pile)

        assert len(discard_pile) == starting_discard_size + expected_discard_size
        assert len(player.hand) == expected_hand_size_eot
