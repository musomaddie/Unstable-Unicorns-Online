import copy

import pytest

from game_details.card import Card, CardType
from game_details.card.factory import card_factory
from game_details.deck import Deck
from game_details.deck.factory import deck_factory
from game_details.discard_pile import DiscardPile
from game_details.discard_pile.factory import discard_pile_factory
from game_details.game import Game
from game_details.nursery import Nursery
from game_details.nursery.factory import nursery_factory
from game_details.player import Player
from game_details.player.factory import player_factory, all_players_factory


@pytest.fixture
def fake_card() -> Card:
    """ Creates a basic card for use in tests. """
    return card_factory.create_default("Name", CardType.BASIC_UNICORN)


@pytest.fixture
def discard_pile() -> DiscardPile:
    """ Returns an empty discard pile. """
    return discard_pile_factory.create_default()


@pytest.fixture
def nursery() -> Nursery:
    """ Returns a nursery. """
    return nursery_factory.create_default()


@pytest.fixture
def three_player_list() -> list[Player]:
    """ Returns a list of three players (Aelin, Chaol and Dorian). """
    return [
        create_default_player("Aelin"),
        create_default_player("Chaol"),
        create_default_player("Dorian")
    ]


@pytest.fixture
def deck() -> Deck:
    """ Returns a deck """
    return deck_factory.create(card_factory.create_all())


@pytest.fixture
def fake_deck() -> Deck:
    """ Returns a deck with fake cards that are all confirmed to be different. """
    return deck_factory.create(
        [card_factory.create_default(f"Card #{i}", CardType.BASIC_UNICORN) for i in range(100)]
    )


@pytest.fixture
def game(fake_deck, discard_pile, nursery, three_player_list) -> Game:
    """ Returns a game for testing. """
    return Game(
        fake_deck,
        discard_pile,
        nursery,
        all_players_factory.create([player for player in three_player_list])
    )


def create_default_player(name: str) -> Player:
    """ Creates a player with the given name. """
    return player_factory.create_default(name)


def create_deck_with_special_first_card(first_card: Card, other_card: Card) -> Deck:
    """ Creates and returns a deck with the given first card, and 10 copies of the second card. """
    deck = deck_factory.create_one_card(first_card)
    for _ in range(10):
        deck.cards.append(copy.copy(other_card))
    return deck
