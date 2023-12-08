""" all players file """
from dataclasses import dataclass

from game_details.player.player import Player


@dataclass
class AllPlayers:
    """ Manages all the players within the game."""

    players: list[Player]

    def __len__(self) -> int:
        return len(self.players)

    def __getitem__(self, item) -> Player:
        return self.players[item]

    def __iter__(self) -> 'AllPlayersIterator':
        return AllPlayersIterator(self)


class AllPlayersIterator:
    """ An iterator for the all players object. """

    def __init__(self, all_players: AllPlayers):
        self._all_players = all_players
        self._index = 0

    def __next__(self) -> Player:
        if self._index < len(self._all_players):
            self._index += 1
            return self._all_players[self._index - 1]
        raise StopIteration
