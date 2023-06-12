from game_details.player import Player


class AllPlayersManager:
    """ Manages all the players within the game."""

    def __init__(self, players=list[Player]):
        self.players = players
