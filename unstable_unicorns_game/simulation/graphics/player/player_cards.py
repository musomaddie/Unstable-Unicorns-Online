""" area for cards to be displayed. """
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.hand_ui import HandUi
from unstable_unicorns_game.simulation.graphics.player.stable_ui import StableUi
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget


def _create_expanded_view(hand: HandUi, stable: StableUi) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.add_widgets(
        hand.expanded_view,
        stable.expanded_view
    )
    return widget


def _create_compact_view(hand: HandUi, stable: StableUi) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.add_widgets(
        hand.compact_view,
        stable.compact_view
    )
    return widget


def _create_turn_view(hand: HandUi, stable: StableUi) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.add_widgets(
        hand.turn_view,
        stable.turn_view
    )

    return widget


class PlayerCardsUi:
    """ Contains all the cards the player has, including their hand and stable. """
    # TODO -> figure out somehow to make sure this all updates when the underlying data changes.
    hand: HandUi
    stable: StableUi

    expanded_view: ContainerWidget
    turn_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, player: Player):
        self.player = player
        self.hand = HandUi(player.hand)
        self.stable = StableUi(player.stable)

        self.expanded_view = _create_expanded_view(self.hand, self.stable)
        self.compact_view = _create_compact_view(self.hand, self.stable)
        self.turn_view = _create_turn_view(self.hand, self.stable)

    def update_hand_view(self):
        self.hand.update_view()

    def enable_hand_choice(self, on_click: Callable[[Card], None]):
        self.hand.enable_card_selection(on_click)

    def disable_hand_choice(self):
        self.hand.disable_card_selection()
