""" all players file """
from dataclasses import dataclass

from unstable_unicorns_game.game.player.player import Player


@dataclass
class AllPlayers:
    """ Manages all the players within the game."""

    players: list[Player]
    current_player_idx: int = 0

    def __len__(self) -> int:
        return len(self.players)

    def __getitem__(self, item) -> Player:
        return self.players[item]

    def __iter__(self):
        yield from self.players

    @classmethod
    def create(cls, players: list[Player]) -> 'AllPlayers':
        return cls(players)

    @classmethod
    def create_default(cls) -> 'AllPlayers':
        return cls.create([])

    def current_player(self) -> Player:
        """ Returns the current player. """
        return self.players[self.current_player_idx % len(self.players)]

    def next_player(self) -> None:
        """ Moves to the next player's turn. """
        self.current_player_idx += 1

