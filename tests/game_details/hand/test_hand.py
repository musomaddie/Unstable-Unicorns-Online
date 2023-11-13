""" Tests for hand. """
import copy
from io import StringIO

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType
from game_details.hand import Hand


@pytest.fixture
def hand() -> Hand:
    """ Hand for tests"""
    return Hand.create_default()


@fixture
def hand_with_cards() -> Hand:
    """ A hand populated with multiple cards. """
    return Hand([
        Card.create_default("Unicorn", CardType.BASIC_UNICORN),
        Card.create_default("Second unicorn", CardType.MAGIC_UNICORN)])


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
        return Hand([copy.copy(card) for _ in range(n)])

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

    def test_no_cards_no_output(self, hand, capsys):
        result = hand.choose_card_to_discard()

        assert result is None
        assert len(hand) == 0
        assert capsys.readouterr().out == "You have no cards.\n"

    def test_with_one_card(self, monkeypatch, capsys):
        card = Card.create_default("Only card", CardType.BASIC_UNICORN)
        hand = Hand([card])
        monkeypatch.setattr("sys.stdin", StringIO("1"))

        result = hand.choose_card_to_discard()

        assert result == card
        expected_lines = [
            "[1]\tOnly card (Basic Unicorn): default text",
            "Choose (1): "
        ]
        assert capsys.readouterr().out == "\n".join(expected_lines)
        assert len(hand) == 0

    def test_cards_with_failed_attempts(self, hand_with_cards, monkeypatch, capsys):
        monkeypatch.setattr("sys.stdin", StringIO("-1\noops\n2"))

        result = hand_with_cards.choose_card_to_discard()

        assert result.name == "Second unicorn"
        expected_lines = [
            "[1]\tUnicorn (Basic Unicorn): default text",
            "[2]\tSecond unicorn (Magic Unicorn): default text",
            "Choose (1|2): Could not understand -1, please try again.",
            "Choose (1|2): Could not understand oops, please try again.",
            "Choose (1|2): "
        ]
        assert len(hand_with_cards) == 1
        assert capsys.readouterr().out == "\n".join(expected_lines)
