""" Tests for hand. """
import copy

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType
from game_details.card.factory import card_factory
from game_details.hand import Hand
from game_details.hand.factory import hand_factory
from game_details.player.factory import player_factory
from game_details.stable.factory import stable_factory
from play_deciders import DeciderFactory, DeciderType


@pytest.fixture
def hand() -> Hand:
    """ Hand for tests"""
    return hand_factory.create_default()


@fixture
def hand_with_cards() -> Hand:
    """ A hand populated with multiple cards. """
    return hand_factory.create([
        card_factory.create_default("Unicorn", CardType.BASIC_UNICORN),
        card_factory.create_default("Second unicorn", CardType.MAGIC_UNICORN)])


def test_constructor_default(hand):
    assert len(hand) == 0
    assert hand.limit == 7


def test_add_card(hand, fake_card):
    num_cards_before = len(hand)

    hand.add_card(fake_card)

    assert len(hand) == num_cards_before + 1
    assert hand.cards[-1] == fake_card


class TestMustDiscardToLimit:
    @staticmethod
    def make_hand_with_n_cards(n: int, card: Card) -> Hand:
        """ returns a hand that contains the given number of cards. """
        return hand_factory.create([copy.copy(card) for _ in range(n)])

    def test_8_cards_true(self, fake_card):
        hand = self.make_hand_with_n_cards(8, fake_card)
        assert hand.must_discard_to_limit()

    def test_7_cards_false(self, fake_card):
        hand = self.make_hand_with_n_cards(7, fake_card)
        assert not hand.must_discard_to_limit()

    def test_6_cards_false(self, fake_card):
        hand = self.make_hand_with_n_cards(6, fake_card)
        assert not hand.must_discard_to_limit()


class TestPrintBasicsWithIndex:

    def test_with_cards(self, hand_with_cards, capsys):
        expected_u1 = "[1]\tUnicorn (Basic Unicorn): default text"
        expected_u2 = "[2]\tSecond unicorn (Magic Unicorn): default text"
        expected = f"{expected_u1}\n{expected_u2}\n"

        hand_with_cards.print_basics_with_index()

        assert capsys.readouterr().out == expected

    def test_without_cards(self, hand, capsys):
        hand.print_basics_with_index()

        assert capsys.readouterr().out == "You have no cards.\n"


class TestChooseCardToDiscard:

    def test_no_cards(self, hand):
        player = player_factory.create("Test", hand, stable_factory.create_default(), DeciderFactory(DeciderType.QUEUE))
        result = player.hand.choose_card_to_discard()

        assert result is None
        assert len(hand) == 0

    def test_with_cards(self, hand_with_cards):
        player = player_factory.create(
            "Test", hand_with_cards, stable_factory.create_default(), DeciderFactory(DeciderType.QUEUE))
        result = player.hand.choose_card_to_discard()

        assert result.name == "Unicorn"
        assert len(player.hand) == 1

    def test_without_decider(self):
        hand = hand_factory.create_default()
        with pytest.raises(TypeError):
            hand.choose_card_to_discard()
