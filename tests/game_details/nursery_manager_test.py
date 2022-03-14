import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.NurseryManager import NurseryManager

@pytest.fixture
def nursery():
    return NurseryManager()

def test_setup(nursery):
    assert len(nursery.cards) == 30

def test_remove_from_nursery(nursery):
    card = nursery.remove_from_nursery()
    assert card.name_equals("Baby Unicorn")
    assert len(nursery.cards) == 29
