""" overall board for the player. """
from enum import auto, Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.card_area import CardArea
from unstable_unicorns_game.simulation.graphics.widget import Widget


class ViewMode(Enum):
    """ View mode for THIS players board. """
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()
    SUMMARISED = auto()


class PlayerBoard(Widget):
    """ Contains the entire player board. """

    def __init__(self, player: Player, color_code: str):
        super().__init__(layout=QHBoxLayout())
        self.view_mode = ViewMode.OVERVIEW
        self.color_code = color_code

        self.style_with_selectors(self.get_styling())

        # I suspect this will be helpful ->
        # https://stackoverflow.com/questions/10416582/replacing-layout-on-a-qwidget-with-another-layout

        # This is all for overview styling, I'm not sure what should stay in the init vs what shouldn't.
        self.name_lbl = QLabel(player.name)
        self.name_lbl.setObjectName("name")
        self.name_lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        lbl_sp = self.name_lbl.sizePolicy()
        lbl_sp.setHorizontalStretch(1)
        self.name_lbl.setSizePolicy(lbl_sp)

        self.card_area = CardArea(player)
        cards_sp = self.card_area.widget.sizePolicy()
        cards_sp.setHorizontalStretch(3)
        self.card_area.widget.setSizePolicy(cards_sp)

        self.add_widgets(
            self.name_lbl,
            self.card_area.widget)

    def get_styling(self):
        if self.view_mode == ViewMode.OVERVIEW:
            return {
                "*": {
                    "background-color": self.color_code,
                    # "font-family": "Itim",
                },
                "#name": {
                    # "font-family": "Manhattan Darling",
                    "font-size": "50px"
                }
            }

        # TODO -> styling for other view modes
        return {}

    def update_view_mode(self, view_mode: ViewMode):
        self.card_area.update_view_mode()
        # TODO -> properly implement
