import copy
from io import StringIO

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType
from game_details.hand import Hand


@pytest.fixture
def hand():
    return Hand()


@fixture
def hand_with_cards():
    return Hand([
        Card("Unicorn", CardType.BASIC_UNICORN, "I am some text, hello!"),
        Card("Second unicorn", CardType.MAGIC_UNICORN, "omg magic")])


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
        return Hand([copy.copy(card) for _ in range(n)])

    def test_8_cards_true(self, fake_card):
        hand = self.make_hand_with_n_cards(8, fake_card)
        assert hand.must_discard_to_limit()

    def test_7_cards_true(self, fake_card):
        hand = self.make_hand_with_n_cards(7, fake_card)
        assert hand.must_discard_to_limit()

    def test_6_cards_false(self, fake_card):
        hand = self.make_hand_with_n_cards(6, fake_card)
        assert not hand.must_discard_to_limit()


class TestPrintBasicsWithIndex:

    def test_with_cards(self, hand_with_cards, capsys):
        expected_u1 = "[0]\tUnicorn (Basic Unicorn): I am some text, hello!"
        expected_u2 = "[1]\tSecond unicorn (Magic Unicorn): omg magic"
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
        card = Card("Only card", CardType.BASIC_UNICORN, "text")
        hand = Hand([card])
        monkeypatch.setattr("sys.stdin", StringIO("0"))

        result = hand.choose_card_to_discard()

        assert result == card
        expected_lines = [
            "[0]\tOnly card (Basic Unicorn): text",
            "Choose (0): "
        ]
        assert capsys.readouterr().out == "\n".join(expected_lines)
        assert len(hand) == 0

    def test_cards_with_failed_attempts(self, hand_with_cards, monkeypatch, capsys):
        monkeypatch.setattr("sys.stdin", StringIO("-1\noops\n1"))

        result = hand_with_cards.choose_card_to_discard()

        assert result.name == "Second unicorn"
        expected_lines = [
            "[0]\tUnicorn (Basic Unicorn): I am some text, hello!",
            "[1]\tSecond unicorn (Magic Unicorn): omg magic",
            "Choose (0|1): Could not understand -1, please try again.",
            "Choose (0|1): Could not understand oops, please try again.",
            "Choose (0|1): "
        ]
        assert len(hand_with_cards) == 1
        assert capsys.readouterr().out == "\n".join(expected_lines)
