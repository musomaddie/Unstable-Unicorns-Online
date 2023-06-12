import pytest

from game_details.card import Card, CardType


@pytest.fixture
def fake_card():
    return Card("Name", CardType.BASIC_UNICORN, "Text")
