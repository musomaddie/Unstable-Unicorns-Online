""" list of all players. """
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from unstable_unicorns_game.game_details.player import AllPlayers
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
    @classmethod
    def create_widget(cls, players: AllPlayers) -> QWidget:
        return cls(players).widget

    def __init__(self, players: AllPlayers):
        super().__init__(QVBoxLayout())

        self.add_widgets(
            *[PlayerBoard.create_widget(player, color_code) for player, color_code in zip(players, color_list)]
        )
