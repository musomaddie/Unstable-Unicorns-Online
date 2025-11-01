""" overall board for the player. """
from enum import auto, Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.card_area import CardArea
from unstable_unicorns_game.simulation.graphics.widget import ContainerWidget


def overview_styling(colour_code: str):
    return {
        "*": {
            "background-color": colour_code,
            # "font-family": "Itim",
        },
        "#name": {
            # "font-family": "Manhattan Darling",
            "font-size": "50px"
        }}


def create_name_label(name: str):
    lbl = QLabel(name)
    lbl.setObjectName("name")
    lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
    # Size policy
    lbl_sp = lbl.sizePolicy()
    lbl_sp.setHorizontalStretch(1)
    lbl.setSizePolicy(lbl_sp)

    return lbl


def create_card_area(player: Player):
    card_area = CardArea(player)
    cards_sp = card_area.widget.sizePolicy()
    cards_sp.setHorizontalStretch(3)
    card_area.widget.setSizePolicy(cards_sp)

    return card_area


def create_initial_label(player_name: str):
    """ Creates an initial label for the player. """


class PlayerViewMode(Enum):
    """ View mode for THIS players board. """
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()
    SUMMARISED = auto()


class PlayerBoard(ContainerWidget):
    """ Contains the entire player board. """

    player: Player
    view_mode: PlayerViewMode
    color_code: str

    # Widgets
    name_lbl: QLabel
    card_area: CardArea
    initial_lbl: QLabel

    def __init__(self, player: Player, color_code: str):
        super().__init__(layout=QHBoxLayout())
        self.player = player
        self.view_mode = PlayerViewMode.OVERVIEW
        self.color_code = color_code

        self.name_lbl = create_name_label(player.name)
        self.card_area = create_card_area(player)
        # self.initial_lbl = QLabel("Initial")

        self.style_with_selectors(self.get_styling())
        self.add_qwidget(self.name_lbl)
        self.add_widgets(self.card_area)

    def get_styling(self):
        if self.view_mode == PlayerViewMode.OVERVIEW:
            return overview_styling(self.color_code)

        # TODO -> styling for other view modes
        return {}

    def update_view_mode(self, view_mode: PlayerViewMode):
        self.card_area.update_view_mode()
        # TODO -> properly implement
