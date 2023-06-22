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
def holder(first_card, second_card, third_card):
    return MultipleCardsHolder([first_card, second_card, third_card])


def test_len(holder):
    assert len(holder) == 3


def test_getitem(holder, second_card):
    assert holder[1] == second_card


def test_iterator(holder, first_card, second_card, third_card):
    expected = [first_card, second_card, third_card]
    for actual, expect in zip(holder, expected):
        assert actual == expect
