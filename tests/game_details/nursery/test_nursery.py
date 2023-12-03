""" Nursery tests"""
import pytest

from game_details.card import CardType
from game_details.nursery import Nursery
from game_details.nursery.factory import nursery_factory


@pytest.fixture
def nursery() -> Nursery:
    """ Creates a default nursery """
    return nursery_factory.create_default()


def test_create_default(nursery):
    assert len(nursery) == 25


def test_get_baby(nursery):
    size_before = len(nursery)
    baby = nursery.get_baby()
    assert baby.card_type == CardType.BABY_UNICORN
    assert len(nursery) == size_before - 1
