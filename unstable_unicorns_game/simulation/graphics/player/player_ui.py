""" overall board for the player. """
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_cards import PlayerCardsUi
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.utility.measurements import Margins
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel, Label, RightAlignedLabel


def _create_name_label(name: str) -> Label:
    lbl = RightAlignedLabel(name, style_identifier="name", horizontal_stretch=1)

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
        player_name[0].upper(), horizontal_align=Qt.AlignmentFlag.AlignTop)
    lbl.widget.setObjectName("initial")
    return lbl


def _create_overview_view(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout(), styling=styles.player_board(color_code))

    widget.add_widgets(
        _create_name_label(name), _create_card_area(cards_ui, True))
    return widget


class PlayerSummaryView:
    initial_only_view: ContainerWidget
    detail_view: ContainerWidget

    def __init__(self, name: str, cards_ui: PlayerCardsUi, color_code: str):
        self.detail_view = ContainerWidget(
            QVBoxLayout(),
            styling=styles.player_board(color_code),
            align=Qt.AlignmentFlag.AlignCenter,
            children=[_create_initial_label(name), _create_card_area(cards_ui, False)])
        self.initial_only_view = ContainerWidget(
            QVBoxLayout(),
            styling=styles.player_board(color_code),
            align=Qt.AlignmentFlag.AlignCenter,
            children=[_create_initial_label(name)])
        # self.use_initial_only = False


def _create_summary_view(name: str, cards_ui: PlayerCardsUi, color_code: str) -> ContainerWidget:
    return ContainerWidget(
        QVBoxLayout(), styling=styles.player_board(color_code), align=Qt.AlignmentFlag.AlignCenter, children=[
            _create_initial_label(name), _create_card_area(cards_ui, False)])


class CurrentPlayerWidget(ContainerWidget):
    choice_label: Label

    def __init__(self, name: str, cards_ui: PlayerCardsUi, color_code: str, **kwargs):
        self.choice_label = CenteredLabel("", style_identifier="choice-label")
        self.choice_label.hide()

        super().__init__(
            QVBoxLayout(),
            styling=styles.player_board(color_code),
            margins=Margins(bottom=0),
            children=[
                CenteredLabel(f"{name}'s turn", style_identifier="turn-heading"),
                self.choice_label,
                cards_ui.turn_view],
            **kwargs)

    def update_text(self, text: str):
        self.choice_label.update_text(text)
        if self.choice_label.text != "":
            self.choice_label.show()
        else:
            self.choice_label.hide()


class PlayerUi:
    player: Player

    cards_ui: PlayerCardsUi

    overview_view: ContainerWidget
    current_player_view: CurrentPlayerWidget
    summary_view: PlayerSummaryView

    def __init__(self, player: Player, color_code: str):
        self.player = player
        self.color_code = color_code

        self.cards_ui = PlayerCardsUi(player)

        self.overview_view = _create_overview_view(player.name, self.cards_ui, color_code)
        self.current_player_view = CurrentPlayerWidget(player.name, self.cards_ui, color_code)
        # self.summary_view = _create_summary_view(player.name, self.cards_ui, color_code)
        self.summary_view = PlayerSummaryView(player.name, self.cards_ui, color_code)

    def update_view(self, hand: bool = False, stable: bool = False):
        self.cards_ui.update_view(hand, stable)

    def update_user_choice_text(self, text: str):
        self.current_player_view.update_text(text)

    def enable_card_choice(self, on_click: Callable[[Card], None]):
        """ Enable choosing a card to play. """
        self.cards_ui.enable_card_choice(on_click)

    def disable_card_choice(self):
        self.cards_ui.disable_card_choice()
