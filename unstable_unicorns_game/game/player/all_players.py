""" all players file """
from dataclasses import dataclass

import unstable_unicorns_game.utilities.logger_keys as LK
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.utilities.logger import Logger


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

    def create_log(self) -> Logger:
        """ Returns a dictionary of the current players to be used in the log file at the start of a game."""
        return Logger({
            LK.N_PLAYERS: len(self),
            LK.PLAYER_NAMES: [player.name for player in self],
            LK.PLAYER_IDS: [player.id for player in self],
        })

    def debug_str(self, indents: int = 0) -> str:
        """ Returns a string (possibly multi-line) describing the current state of the players."""
        return "\n".join(
            [("\t" * indents + f"{'Players':<8} :")] + [
                player.debug_str(indents=indents + 1) for player in self]
        )

    def current_player(self) -> Player:
        """ Returns the current player. """
        return self.players[self.current_player_idx % len(self.players)]

    def next_player(self) -> None:
        """ Moves to the next player's turn. """
        self.current_player_idx += 1
