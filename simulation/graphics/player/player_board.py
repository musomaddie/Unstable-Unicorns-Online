""" overall board for the player. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout

from simulation.graphics.player.card_area import CardArea
from simulation.graphics.utility import Widget


class PlayerBoard(Widget):
    """ Contains the entire player board. """

    def __init__(self, player_name: str):
        super().__init__(layout=QVBoxLayout())
        self.style({"background-color": "#c1d5f5"})

        name_lbl = QLabel(player_name)
        name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout.addWidget(name_lbl)
        self.layout.addWidget(CardArea.create_widget())

    @classmethod
    def create_widget(cls, player_name: str) -> QWidget:
        return cls(player_name).widget
