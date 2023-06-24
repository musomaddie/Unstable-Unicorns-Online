import copy

import pytest
from _pytest.fixtures import fixture

from game_details.card import Card
from game_details.hand import Hand


@pytest.fixture
def hand():
    return Hand()


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

    @fixture
    def hand_with_cards(self):
        return Hand([
            Card.create_card(
                {"name": "Unicorn", "type": "basic unicorn", "text": "I am some text, hello!"}),
            Card.create_card(
                {"name": "Second unicorn", "type": "magic unicorn", "text": "omg magic"})])

    def test_with_cards(self, hand_with_cards, capsys):
        expected_u1 = "[0]\tUnicorn (Basic Unicorn): I am some text, hello!"
        expected_u2 = "[1]\tSecond unicorn (Magic Unicorn): omg magic"
        expected = f"{expected_u1}\n{expected_u2}\n"

        hand_with_cards.print_basics_with_index()

        assert capsys.readouterr().out == expected

    def test_without_cards(self, hand, capsys):
        hand.print_basics_with_index()

        assert capsys.readouterr().out == "You have no cards.\n"
