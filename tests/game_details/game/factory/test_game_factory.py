""" tests for the game factory. """
import pytest

from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.deck.factory import deck_factory
from unstable_unicorns_game.game_details.game import Game
from unstable_unicorns_game.game_details.game.factory import N_STARTING_CARDS
from unstable_unicorns_game.game_details.game.factory import game_factory
from unstable_unicorns_game.game_details.nursery.factory import nursery_factory
from unstable_unicorns_game.play_deciders import DeciderFactory, DeciderType


@pytest.fixture
def player_names():
    """ Returns a list of 3 player names. """
    return ["Aelin", "Chaol", "Dorian"]


@pytest.fixture
def game() -> Game:
    """ Returns a created game with 3 players. """
    return game_factory.create(["Aelin", "Chaol", "Dorian"], DeciderFactory(DeciderType.QUEUE))


def test_deck_fullDeckWithoutDealtCards(game):
    """ Asserts the deck within the game is all the created cards, minus the ones that have been dealt. """
    expected_deck = deck_factory.create(card_factory.create_all())
    number_of_allocated_cards = len(game.players) * N_STARTING_CARDS

    assert len(game.deck) == len(expected_deck) - number_of_allocated_cards


def test_discardPile_isEmpty(game):
    """ Asserts the discard pile created at the start of the game is empty. """
    assert len(game.discard_pile) == 0


def test_nursery_fullNurseryWithoutPlayerBabies(game):
    """ Asserts the nursery contains all the babies besides the ones allocated to the players. """
    expected_nursery = nursery_factory.create_default()
    number_allocated_babies = len(game.players)

    assert len(game.nursery) == len(expected_nursery) - number_allocated_babies
