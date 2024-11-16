""" Factory for creating Hand instances."""
from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.game_details.hand.impl.hand_impl import HandImpl
from unstable_unicorns_game.play_deciders import decider_factory
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


def create(cards: list[Card], decider: PlayDecider) -> Hand:
    """ Creates a hand containing the given cards. """
    # TODO -> modify this to not take in a list of cards. Makes sense to create an empty hand which is progressively
    #  adde
    # d to. (or otherwise use a builder).
    hand = HandImpl(cards)
    hand.decider = decider.create_discard_decider(hand)
    return hand


def create_only_cards(cards: list[Card]) -> Hand:
    """ Creates a hand from only cards. """
    return create(cards, decider_factory.create("queue"))


def create_default() -> Hand:
    """ Creates a hand with an empty list. """
    return create_only_cards(cards=[])
