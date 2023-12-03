""" Factory for creating DiscardPile instances. """
from game_details.card import Card
from game_details.discard_pile import DiscardPile


def create_default() -> DiscardPile:
    """ Creates an empty discard pile. """
    return DiscardPile(cards=[])


def create(cards: list[Card]) -> DiscardPile:
    """ Creates a discard pile with the given list of cards. """
    return DiscardPile(cards)
