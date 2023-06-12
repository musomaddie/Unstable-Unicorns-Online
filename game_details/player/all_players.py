from dataclasses import dataclass

from game_details.player.player import Player


@dataclass
class AllPlayers:
    """ Manages all the players within the game."""

    players: list[Player]
