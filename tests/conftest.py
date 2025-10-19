import copy

import pytest

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.game.cards.nursery import Nursery
from unstable_unicorns_game.game.game import Game, load_all_cards
from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player


@pytest.fixture
def fake_card() -> Card:
    """ Creates a basic card for use in tests. """
    return Card.create_default("Name", CardType.BASIC_UNICORN)


@pytest.fixture
def discard_pile() -> DiscardPile:
    """ Returns an empty discard pile. """
    return DiscardPile.create_default()


@pytest.fixture
def nursery() -> Nursery:
    """ Returns a nursery. """
    return Nursery.create_default()


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
    return Deck.create(load_all_cards())


@pytest.fixture
def fake_deck() -> Deck:
    """ Returns a deck with fake cards that are all confirmed to be different. """
    return Deck.create([Card.create_default(f"Card #{i}", CardType.BASIC_UNICORN) for i in range(100)])


@pytest.fixture
def game(fake_deck, discard_pile, nursery, three_player_list) -> Game:
    """ Returns a game for testing. """
    return Game(
        fake_deck,
        discard_pile,
        nursery,
        AllPlayers.create([player for player in three_player_list])
    )


def create_default_player(name: str) -> Player:
    """ Creates a player with the given name. """
    return Player.create_default(name)


def create_deck_with_special_first_card(first_card: Card, other_card: Card) -> Deck:
    """ Creates and returns a deck with the given first card, and 10 copies of the second card. """
    deck = Deck.create_one_card(first_card)
    for _ in range(10):
        deck.cards.append(copy.copy(other_card))
    return deck
