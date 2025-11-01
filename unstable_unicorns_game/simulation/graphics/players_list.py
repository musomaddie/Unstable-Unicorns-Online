""" list of all players. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.simulation.graphics.player import PlayerBoard
from unstable_unicorns_game.simulation.graphics.utility import Widget

color_list = [
    "#DEDAF4",
    "#D9EDF8",
    "#E4F1EE",
    "#FDFFB6",
    "#FFD6A5",
    "#FFADAD",
]


class PlayersList(Widget):

    def __init__(self, players: AllPlayers):
        super().__init__(QVBoxLayout())

        self.add_widgets(
            *[PlayerBoard(player, color_code).widget for player, color_code in zip(players, color_list)]
        )
