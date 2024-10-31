""" overall board for the player. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout

from game_details.player import Player
from simulation.graphics.player.card_area import CardArea
from simulation.graphics.utility import Widget


class PlayerBoard(Widget):
    """ Contains the entire player board. """

    def __init__(self, player: Player, color_code: str):
        super().__init__(layout=QHBoxLayout())
        self.style_with_selectors({
            "*": {
                "background-color": color_code,
                "font-family": "Itim",
            },
            "#name": {
                "font-family": "Manhattan Darling",
                "font-size": "50px"
            }}
        )

        name_lbl = QLabel(player.name)
        name_lbl.setObjectName("name")
        name_lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        lbl_sp = name_lbl.sizePolicy()
        lbl_sp.setHorizontalStretch(1)
        name_lbl.setSizePolicy(lbl_sp)

        cards = CardArea.create_widget(player)
        cards_sp = cards.sizePolicy()
        cards_sp.setHorizontalStretch(3)
        cards.setSizePolicy(cards_sp)

        self.add_widgets(
            name_lbl,
            cards)

    @classmethod
    def create_widget(cls, player: Player, color_code: str) -> QWidget:
        return cls(player, color_code).widget
