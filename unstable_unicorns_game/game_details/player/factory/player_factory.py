""" Player factory. """
from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.player import Player
from unstable_unicorns_game.game_details.player.impl.player_impl import PlayerImpl
from unstable_unicorns_game.game_details.stable import Stable
from unstable_unicorns_game.game_details.stable.factory import stable_factory


def create(name: str, hand: Hand, stable: Stable) -> Player:
    """ Creates and returns a player. """
    return PlayerImpl(name, hand, stable)


def create_default(name: str) -> Player:
    """ Creates a player with the given name and otherwise default values. """
    return create(name, hand_factory.create_default(), stable_factory.create_default())
