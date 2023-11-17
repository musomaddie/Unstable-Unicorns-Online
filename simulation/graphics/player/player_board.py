""" overall board for the player. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout

from simulation.graphics.player.card_area import CardArea
from simulation.graphics.utility import Widget


class PlayerBoard(Widget):
    """ Contains the entire player board. """

    def __init__(self, player_name: str, condensed: bool):
        super().__init__(layout=QHBoxLayout() if condensed else QVBoxLayout())
        self.style({"background-color": "#c1d5f5"})

        name_lbl = QLabel(player_name)
        name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(name_lbl, CardArea.create_widget(condensed))

    @classmethod
    def create_widget(cls, player_name: str, condensed: bool) -> QWidget:
        return cls(player_name, condensed).widget
