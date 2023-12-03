""" Tests for multiple card holder. """
import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType, MultipleCardsHolder
from game_details.card.factory import card_factory


@fixture
def first_card() -> Card:
    """ Creates a card with name representing it's the first card in the list. """
    return card_factory.create_default("Number 1", CardType.BASIC_UNICORN)


@fixture
def second_card() -> Card:
    """ Creates a card with a name corresponding to its placement as second card in the list"""
    return card_factory.create_default("Number 2", CardType.INSTANT)


@fixture
def third_card() -> Card:
    """ Creates a card to be the third card in the list. """
    return card_factory.create_default("Number 3", CardType.MAGIC)


@fixture
def not_present_card() -> Card:
    """ Creates a card that shouldn't be present in the list. """
    return card_factory.create_default("Shouldn't be present", CardType.DOWNGRADE)


@fixture
def holder(first_card, second_card, third_card) -> MultipleCardsHolder:
    """ Creates a default holder. """
    return MultipleCardsHolder([first_card, second_card, third_card])


def test_len(holder):
    assert len(holder) == 3


def test_getitem(holder, second_card):
    assert holder[1] == second_card


class TestContains:
    def test_does_contain(self, holder, first_card):
        assert first_card in holder

    def test_doesnt_contain(self, holder, not_present_card):
        assert not_present_card not in holder


def test_iterator(holder, first_card, second_card, third_card):
    expected = [first_card, second_card, third_card]
    for actual, expect in zip(holder, expected):
        assert actual == expect


class TestRemove:
    def test_remove_present(self, holder, first_card):
        length_before = len(holder)
        holder.remove(first_card)

        assert first_card not in holder
        assert len(holder) == length_before - 1

    def test_remove_not_present(self, holder, not_present_card):
        with pytest.raises(ValueError) as execinfo:
            holder.remove(not_present_card)

        assert str(not_present_card) in str(execinfo.value)
