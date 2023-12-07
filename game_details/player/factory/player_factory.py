""" Player factory. """
from game_details.hand import Hand
from game_details.hand.factory import hand_factory
from game_details.player import Player
from game_details.player.impl.player_impl import PlayerImpl
from game_details.stable import Stable
from game_details.stable.factory import stable_factory


def create(name: str, hand: Hand, stable: Stable) -> Player:
    """ Creates and returns a player. """
    return PlayerImpl(name, hand, stable)


def create_default(name: str) -> Player:
    """ Creates a player with the given name and otherwise default values. """
    return create(name, hand_factory.create_default(), stable_factory.create_default())
