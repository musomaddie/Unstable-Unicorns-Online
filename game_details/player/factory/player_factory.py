""" Player factory. """
from game_details.hand import Hand
from game_details.player import Player
from game_details.player.impl.player_impl import PlayerImpl
from game_details.stable import Stable
from play_deciders import DeciderFactory


def create(name: str, hand: Hand, stable: Stable, play_decider_factory: DeciderFactory) -> Player:
    """ Creates and returns a player. """
    player = PlayerImpl(name, hand, stable)
    player.hand.connect_play_decider(play_decider_factory.create(player))
    return player


def create_default(name: str) -> Player:
    """ Creates a player with the given name and otherwise default values. """
    return PlayerImpl(name, Hand.create_default(), Stable.create_default())
