""" player hand board area. """
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def create_expanded_view(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.style_with_selectors(styles.player_ui_labels)
    widget.add_widgets(
        RightAlignedLabel("Hand", style_identifier="lbl"),
        CardsRow(cards)
    )
    return widget


def create_compact_view(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout(), style_identifier="container")
    widget.add_widgets(CenteredLabel(str(len(cards))))

    widget.size(styles.CARD_WIDTH, styles.CARD_HEIGHT)
    widget.style_with_selectors(styles.compact_card_pile_for_player_hand)

    return widget


class HandUi:
    hand: Hand

    expanded_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, hand: Hand):
        self.hand = hand

        self.expanded_view = create_expanded_view(hand.cards)
        self.compact_view = create_compact_view(hand.cards)
