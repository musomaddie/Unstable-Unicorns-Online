""" Nursery tests"""
import pytest

from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.nursery import Nursery


@pytest.fixture
def nursery() -> Nursery:
    """ Creates a default nursery """
    return Nursery.create_default()


def test_create_default(nursery):
    assert len(nursery) == 25


def test_get_baby(nursery):
    size_before = len(nursery)
    baby = nursery.get_baby()
    assert baby.card_type == CardType.BABY_UNICORN
    assert len(nursery) == size_before - 1
