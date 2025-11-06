""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.simulation.graphics.cards.cards import CardViewMode, CardsRow
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


class HandBoard(ContainerWidget):
    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        # I wonder if it makes sense for this to be internally stored this many levels deep or if it should be
        # managed through methods like "applyExpandedStyling" called from a higher level? I don't suppose it really
        # matters tbh.
        self.view_mode = CardViewMode.EXPANDED
        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        self.label = RightAlignedLabel("Hand", style_identifier="lbl")
        self.cards = CardsRow(hand.cards)
        # self.compact_widget = CompactHandBoard()
        # This applies the layout stuff for the EXPANDED view, the widgets don't really do anything until they're
        # added
        self.add_widgets(self.label, self.cards)
        self.layout.setAlignment(self.cards.widget, Qt.AlignmentFlag.AlignLeft)

    def _make_compact(self):
        print("making this compact")
        # self.add_widgets(self.compact_widget)

        self.label.clear_layout()
        self.cards.clear_layout()

    def update_view_mode(self, view_mode: CardViewMode):
        """ Applies the given view mode. Does nothing if this is the same as the current view mode."""
        if view_mode == self.view_mode:
            return

        self.view_mode = view_mode
        if view_mode == CardViewMode.COMPACT:
            self._make_compact()

        # TODO -> implement for EXTENDED.
