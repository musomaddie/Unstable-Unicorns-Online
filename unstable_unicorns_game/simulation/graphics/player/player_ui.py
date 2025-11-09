""" overall board for the player. """

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_cards import PlayerCardsUi
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, Label, RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def _create_name_label(name: str) -> Label:
    lbl = RightAlignedLabel(name, style_identifier="name")
    lbl.horizontal_stretch(1)

    return lbl


def _create_card_area(cards_ui: PlayerCardsUi, expanded: bool) -> ContainerWidget:
    # TODO -> make this better - this styling is only for the expanded version.
    if expanded:
        widget = cards_ui.expanded_view
        widget.horizontal_stretch(3)
    else:
        widget = cards_ui.compact_view

    return widget


def _create_initial_label(player_name: str):
    lbl = CenteredLabel(
        player_name[0].upper(),
        horizontal_align=Qt.AlignmentFlag.AlignTop)
    lbl.widget.setObjectName("initial")
    return lbl


def _create_overview_view(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.style_with_selectors(styles.player_board(color_code))

    widget.add_widgets(
        _create_name_label(name),
        _create_card_area(cards_ui, True)
    )
    return widget


def _create_summary_view(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.style_with_selectors(styles.player_board(color_code))
    widget.add_widgets(
        _create_initial_label(name),
        _create_card_area(cards_ui, False)
    )
    widget.align(Qt.AlignmentFlag.AlignCenter)
    return widget


def _create_current_player_view(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.add_widgets(
        CenteredLabel(f"{name}'s turn", style_identifier="turn-heading"),
        cards_ui.turn_view, )
    widget.set_margins(bottom=0)
    widget.style_with_selectors(styles.player_board(color_code))

    return widget


class PlayerUi:
    player: Player

    cards_ui: PlayerCardsUi

    overview_view: ContainerWidget
    current_player_view: ContainerWidget
    summary_view: ContainerWidget

    def __init__(self, player: Player, color_code: str):
        self.player = player
        self.color_code = color_code

        self.cards_ui = PlayerCardsUi(player)

        self.overview_view = _create_overview_view(player.name, self.cards_ui, color_code)
        self.current_player_view = _create_current_player_view(player.name, self.cards_ui, color_code)
        self.summary_view = _create_summary_view(player.name, self.cards_ui, color_code)
