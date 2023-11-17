""" list of all players. """
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from game_details.player import AllPlayers
from simulation.graphics.player import PlayerBoard
from simulation.graphics.utility import Widget


class PlayersList(Widget):
    @classmethod
    def create_widget(cls, players: AllPlayers) -> QWidget:
        return cls(players).widget

    def __init__(self, players: AllPlayers):
        super().__init__(QVBoxLayout())

        self.add_widgets(
            *[
                PlayerBoard.create_widget(player, condensed=index != 0)
                for index, player in enumerate(players)
            ]
        )
