""" overall board for the player. """
from enum import Enum, auto

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.card_area import CardArea
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, Label, RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


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
    return CenteredLabel(
        player_name[0].upper()
    )


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

        self.style_with_selectors(self.get_styling())
        self.add_widgets(self.name_lbl, self.card_area)

    def get_styling(self):
        if self.view_mode == PlayerViewMode.OVERVIEW:
            return overview_styling(self.color_code)

        # TODO -> styling for other view modes -> OR keep styling agnostic to view modes as much as possible ?
        return {}

    def _apply_summarized_styling(self):
        self.add_widgets(self.initial_lbl)

        self.name_lbl.clear_layout()
        self.card_area.clear_layout()

    def update_view_mode(self, view_mode: PlayerViewMode):
        if view_mode == self.view_mode:
            return
        self.view_mode = view_mode
        if view_mode == PlayerViewMode.SUMMARISED:
            self._apply_summarized_styling()

        # TODO -> implement overview and current styling.
