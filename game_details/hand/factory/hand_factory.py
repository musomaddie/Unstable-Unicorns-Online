""" Factory for creating Hand instances."""
from game_details.card import Card
from game_details.hand import Hand
from game_details.hand.impl.hand_impl import HandImpl
from play_deciders import DeciderFactory, DeciderType


# TODO -> test all factories!

def create(cards: list[Card], decider_factory: DeciderFactory) -> Hand:
    """ Creates a hand containing the given cards. """
    hand = HandImpl(cards)
    hand.decider = decider_factory.create_discard(hand)
    return hand


def create_only_cards(cards: list[Card]) -> Hand:
    """ Creates a hand from only cards. """
    return create(cards, decider_factory=DeciderFactory(DeciderType.QUEUE))


def create_default() -> Hand:
    """ Creates a hand with an empty list. """
    return create_only_cards(cards=[])
