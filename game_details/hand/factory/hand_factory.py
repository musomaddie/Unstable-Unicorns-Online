""" Factory for creating Hand instances."""
from game_details.card import Card
from game_details.hand import Hand
from game_details.hand.impl.hand_impl import HandImpl


def create_default() -> Hand:
    """ Creates a hand with an empty list. """
    return HandImpl(cards=[])


def create(cards: list[Card]) -> Hand:
    """ Creates a hand containing the given cards. """
    return HandImpl(cards)
