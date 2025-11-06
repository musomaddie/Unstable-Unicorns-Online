""" overall board for the player. """
from enum import Enum, auto

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.card_area import CardArea
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, Label, RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def styling(colour_code: str):
    return {
        "*": {
            "background-color": colour_code,
            # "font-family": "Itim",
        },
        "#name": {
            # "font-family": "Manhattan Darling",
            "font-size": "50px"
        },
        "#initial": {
            "font-size": "30px"
        }
    }


def create_name_label(name: str) -> Label:
    lbl = RightAlignedLabel(name)
    lbl.widget.setObjectName("name")
    # Size policy
    lbl_sp = lbl.widget.sizePolicy()
    lbl_sp.setHorizontalStretch(1)
    lbl.widget.setSizePolicy(lbl_sp)

    return lbl


def create_card_area(player: Player):
    card_area = CardArea(player)
    cards_sp = card_area.widget.sizePolicy()
    cards_sp.setHorizontalStretch(3)
    card_area.widget.setSizePolicy(cards_sp)

    return card_area


def create_initial_label(player_name: str):
    lbl = CenteredLabel(player_name[0].upper(),
                        horizontal_align=Qt.AlignmentFlag.AlignTop)
    lbl.widget.setObjectName("initial")

    return lbl


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
    name_lbl: Label
    card_area: CardArea
    initial_lbl: Label

    def __init__(self, player: Player, color_code: str):
        super().__init__(layout=QHBoxLayout())
        self.player = player
        self.view_mode = PlayerViewMode.OVERVIEW
        self.color_code = color_code

        self.name_lbl = create_name_label(player.name)
        self.card_area = create_card_area(player)
        self.initial_lbl = create_initial_label(player.name)

        self.style_with_selectors(styling(color_code))
        self.add_widgets(self.name_lbl, self.card_area)

    def _apply_summarized_styling(self):
        # TODO -> this needs to be in a horizontal box when in compact.
        # I wonder will simply changing the layout work??
        self.change_layout(QVBoxLayout())
        self.add_widgets(self.name_lbl, self.initial_lbl)
        # self.add_widgets(self.initial_lbl)
        # self.card_area.update_view_mode(CardViewMode.COMPACT)
        #
        # self.name_lbl.clear_layout()

    def update_view_mode(self, view_mode: PlayerViewMode):
        if view_mode == self.view_mode:
            return
        self.view_mode = view_mode
        if view_mode == PlayerViewMode.SUMMARISED:
            self._apply_summarized_styling()

        # TODO -> implement overview and current styling.
