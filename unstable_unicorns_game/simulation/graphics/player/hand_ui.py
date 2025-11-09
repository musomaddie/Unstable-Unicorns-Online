""" player hand board area. """
from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.cards.card_pile import create_player_compact_card_pile
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import create_row_of_cards
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def _create_expanded_view(cards: MultipleCardsHolder) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.style_with_selectors(styles.player_ui_labels())
    widget.add_widgets(
        RightAlignedLabel("Hand", style_identifier="lbl"),
        create_row_of_cards(cards.cards)
    )
    return widget


def _create_compact_view(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.add_widgets(
        RightAlignedLabel("H: ", style_identifier="compact-lbl"),
        create_player_compact_card_pile(cards)
    )

    widget.style_with_selectors(styles.player_ui_labels(True))

    return widget


def _create_turn_view(hand: Hand) -> ContainerWidget:
    # TODO -> figure out how to make this update well once a card is drawn.
    widget = ContainerWidget(QHBoxLayout())
    cards_row = create_row_of_cards(hand.cards)
    cards_row.horizontal_stretch(1)

    widget.add_widgets(
        CenteredLabel("Hand", style_identifier="cards-label"),
        cards_row
    )

    return widget


class HandUi:
    hand: Hand

    expanded_view: ContainerWidget
    compact_view: ContainerWidget
    turn_view: ContainerWidget

    def __init__(self, hand: Hand):
        self.hand = hand

        self.expanded_view = _create_expanded_view(hand)
        self.compact_view = _create_compact_view(hand.cards)
        self.turn_view = _create_turn_view(hand)
