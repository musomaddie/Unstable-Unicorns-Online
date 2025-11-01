""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow, CardViewMode
from unstable_unicorns_game.simulation.graphics.widget.widget import GROUP_STYLES, ContainerWidget, CARD_HEIGHT, CARD_WIDTH


class CompactHandBoard(ContainerWidget):
    """ Compact hand board. """

    def __init__(self):
        super().__init__(QVBoxLayout())

        self.widget.setObjectName("container")
        self.widget.setFixedSize(CARD_WIDTH, CARD_HEIGHT)
        self.style_with_selectors({
            "*": {
                "background-color": "#00CCCC",
            },
            "#container": {
                "border-style": "dashed",
                "border-radius": "2px",
                "border-width": "2px",
                "border-color": "black"
            }})

        # TODO add the label.


class HandBoard(ContainerWidget):
    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        # I wonder if it makes sense for this to be internally stored this many levels deep or if it should be
        # managed through methods like "applyExpandedStyling" called from a higher level? I don't suppose it really
        # matters tbh.
        self.view_mode = CardViewMode.EXPANDED
        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        self.label = QLabel("Hand")
        self.label.setObjectName("lbl")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.cards = CardsRow(hand.cards)
        self.compact_widget = CompactHandBoard()
        # TODO -> add the styling in here for all the things, all update view mode should do is change what is
        #  attached to the layout.
        # This applies the layout stuff for the EXPANDED view, the widgets don't really do anything until they're
        # added
        self.add_qwidget(self.label)
        self.add_qwidget(self.cards.widget)
        self.layout.setAlignment(self.cards.widget, Qt.AlignmentFlag.AlignLeft)

    def update_view_mode(self, view_mode: CardViewMode):
        """ Applies the given view mode. Does nothing if this is the same as the current view mode."""
        if view_mode == self.view_mode:
            return

        # TODO -> extended styling

        # Compact styling for hand will just be a small gray box with the hand size in it.
        self.layout.addWidget(self.compact_widget.widget)

        self.label.setParent(None)
        self.cards.widget.setParent(None)
