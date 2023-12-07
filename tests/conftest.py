import copy

import pytest

from game_details.card import Card, CardType
from game_details.card.factory import card_factory
from game_details.deck import Deck
from game_details.deck.factory import deck_factory
from game_details.player import Player
from game_details.player.factory import player_factory


@pytest.fixture
def fake_card() -> Card:
    """ Creates a basic card for use in tests. """
    return card_factory.create_default("Name", CardType.BASIC_UNICORN)


def create_default_player(name: str) -> Player:
    """ Creates a player with the given name. """
    return player_factory.create_default(name)


def create_deck_with_special_first_card(first_card: Card, other_card: Card) -> Deck:
    """ Creates and returns a deck with the given first card, and 10 copies of the second card. """
    deck = deck_factory.create_one_card(first_card)
    for _ in range(10):
        deck.cards.append(copy.copy(other_card))
    return deck
