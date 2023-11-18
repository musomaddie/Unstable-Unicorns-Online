""" overall board for the player. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout

from game_details.player import Player
from simulation.graphics.player.card_area import CardArea
from simulation.graphics.utility import Widget


class PlayerBoard(Widget):
    """ Contains the entire player board. """

    def __init__(self, player: Player):
        super().__init__(layout=QHBoxLayout())
        self.style_with_selectors({
            "*": {
                "background-color": "#c1d5f5",
                "font-family": "Itim",
            },
            "#name": {
                "font-family": "Permanent Marker",
                "font-size": "20px"
            }}
        )

        name_lbl = QLabel(player.name)
        name_lbl.setObjectName("name")
        name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(
            name_lbl,
            CardArea.create_widget(player))

    @classmethod
    def create_widget(cls, player: Player) -> QWidget:
        return cls(player).widget
