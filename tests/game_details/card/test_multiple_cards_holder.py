import pytest
from _pytest.fixtures import fixture

from game_details.card import Card, CardType, MultipleCardsHolder


@fixture
def first_card():
    return Card("Number 1", CardType.BASIC_UNICORN, "Text 1")


@fixture
def second_card():
    return Card("Number 2", CardType.INSTANT, "Text 2")


@fixture
def third_card():
    return Card("Number 3", CardType.MAGIC, "Test 3")


@fixture
def not_present_card():
    return Card("Shouldn't be present", CardType.DOWNGRADE, "...")


@fixture
def holder(first_card, second_card, third_card):
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
