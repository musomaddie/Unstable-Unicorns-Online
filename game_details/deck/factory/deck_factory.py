""" Factory for creating Deck instances. """
from game_details.card import Card
from game_details.deck import Deck
from game_details.deck.impl.deck_impl import DeckImpl


def create_default() -> Deck:
    """ Creates a deck with no cards. """
    return DeckImpl(cards=[])


def create_one_card(card: Card) -> Deck:
    """ Creates a deck containing the given card. """
    return DeckImpl(cards=[card])


def create(cards: list[Card]) -> Deck:
    """ Creates a deck containing the given list of card. """
    return DeckImpl(cards)
