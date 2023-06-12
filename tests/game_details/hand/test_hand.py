import pytest

from game_details.hand import Hand


@pytest.fixture
def hand():
    return Hand()


def test_add_card(hand, fake_card):
    num_cards_before = len(hand)

    hand.add_card(fake_card)

    assert len(hand) == num_cards_before + 1
    assert hand.cards[-1] == fake_card
