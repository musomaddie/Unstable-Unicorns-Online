import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.Player import Player
from game_details.StableManager import StableManager
from tests.game_details.setup import find_card_in_db

CARD_DOWNGRADE_NAME = "Barbed Wire"
CARD_UNICORN_NAME = "Angel Unicorn"
CARD_UPGRADE_NAME = "Dragon Protection"

@pytest.fixture
def stable_manager():
    return StableManager(Player("Alice"))

def test_size_empty(stable_manager):
    assert stable_manager.size() == 0

def test_size_all_cats(stable_manager):
    pass

def test_add_unicorn(stable_manager):
    unicorn_card = find_card_in_db(CARD_UNICORN_NAME)
    stable_manager.add_card(unicorn_card)

    assert len(stable_manager.unicorns) == 1
    assert len(stable_manager.upgrades) == 0
    assert len(stable_manager.downgrades) == 0
    assert stable_manager.unicorns[0] == unicorn_card

def test_add_upgrade(stable_manager):
    upgrade_card = find_card_in_db(CARD_UPGRADE_NAME)
    stable_manager.add_card(upgrade_card)

    print(stable_manager.unicorns)

    assert len(stable_manager.unicorns) == 0
    assert len(stable_manager.upgrades) == 1
    assert len(stable_manager.downgrades) == 0
    assert stable_manager.upgrades[0] == upgrade_card

def test_add_downgrade(stable_manager):
    downgrade_card = find_card_in_db(CARD_DOWNGRADE_NAME)
    stable_manager.add_card(downgrade_card)

    assert len(stable_manager.unicorns) == 0
    assert len(stable_manager.upgrades) == 0
    assert len(stable_manager.downgrades) == 1
    assert stable_manager.downgrades[0] == downgrade_card
