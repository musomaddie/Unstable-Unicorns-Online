import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.DeckManager import DeckManager
from tests.game_details.setup import find_card_in_db

CARD_1_NAME = "A Cute Attack"
CARD_2_NAME = "Angel Unicorn"

@pytest.fixture
def example_deck():
    # TODO: possibly include sizes
    cards = [find_card_in_db(CARD_1_NAME), find_card_in_db(CARD_2_NAME)]
    deck = DeckManager(cards)
    return deck

def test_draw_top_card(example_deck):
    returned_card = example_deck.draw_top_card()

    assert returned_card.name_equals(CARD_1_NAME)
    assert len(example_deck.cards) == 1
    assert example_deck.cards[0].name_equals(CARD_2_NAME)
