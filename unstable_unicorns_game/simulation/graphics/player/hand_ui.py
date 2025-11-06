""" player hand board area. """
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow
from unstable_unicorns_game.simulation.graphics.widget.label import RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import CARD_HEIGHT, CARD_WIDTH, ContainerWidget, \
    GROUP_STYLES


def create_expanded_view(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.style_with_selectors(GROUP_STYLES["player_board_labels"])
    widget.add_widgets(
        RightAlignedLabel("Hand", style_identifier="lbl"),
        CardsRow(cards)
    )
    return widget


def create_compact_view(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout(), style_identifier="container")
    widget.size(CARD_WIDTH, CARD_HEIGHT)
    widget.style_with_selectors({
        "*": {
            "background-color": "#00CCCC",
        },
        "#container": {
            "border-style": "dashed",
            "border-radius": "2px",
            "border-width": "2px",
            "border-color": "black"
        }})

    return widget


class HandUi:
    hand: Hand

    expanded_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, hand: Hand):
        self.hand = hand

        self.expanded_view = create_expanded_view(hand.cards)
        self.compact_view = create_compact_view(hand.cards)
