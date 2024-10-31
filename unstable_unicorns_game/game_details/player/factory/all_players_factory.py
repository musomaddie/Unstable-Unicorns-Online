""" Factory for creating AllPlayers instances. """
from unstable_unicorns_game.game_details.player import AllPlayers, Player


def create(players: list[Player]) -> AllPlayers:
    """ Creates an AllPlayers object from the given list of players."""
    return AllPlayers(players)


def create_default() -> AllPlayers:
    """ Creates default. """
    return create(players=[])
