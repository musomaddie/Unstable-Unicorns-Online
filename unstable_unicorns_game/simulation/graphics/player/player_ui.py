""" overall board for the player. """

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_cards import PlayerCardsUi
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
    lbl = RightAlignedLabel(name, style_identifier="name")
    # Size policy
    lbl_sp = lbl.widget.sizePolicy()
    lbl_sp.setHorizontalStretch(1)
    lbl.widget.setSizePolicy(lbl_sp)

    return lbl


def create_card_area(cards_ui: PlayerCardsUi, expanded: bool) -> ContainerWidget:
    # TODO -> make this better - this styling is only for the expanded version.
    if expanded:
        widget = cards_ui.expanded_view
        widget.horizontal_stretch(3)
    else:
        widget = cards_ui.compact_view

    return widget


def create_initial_label(player_name: str):
    lbl = CenteredLabel(
        player_name[0].upper(),
        horizontal_align=Qt.AlignmentFlag.AlignTop)
    lbl.widget.setObjectName("initial")
    return lbl


def create_overview_widget(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.style_with_selectors(styling(color_code))

    widget.add_widgets(
        create_name_label(name),
        create_card_area(cards_ui, True)
    )
    return widget


def create_compact_widget(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.style_with_selectors(styling(color_code))
    widget.add_widgets(
        create_initial_label(name),
        create_card_area(cards_ui, False)
    )
    widget.align(Qt.AlignmentFlag.AlignCenter)
    return widget


class PlayerUi:
    player: Player

    cards_ui: PlayerCardsUi

    overview_widget: ContainerWidget
    current_player_widget: ContainerWidget
    summary_widget: ContainerWidget

    def __init__(self, player: Player, color_code: str):
        self.player = player
        self.color_code = color_code

        self.cards_ui = PlayerCardsUi(player)

        self.overview_widget = create_overview_widget(player.name, self.cards_ui, color_code)
        self.current_player_widget = create_compact_widget(player.name, self.cards_ui, color_code)
