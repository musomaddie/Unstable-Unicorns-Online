""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel

from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.widget import Widget


class CardPileUi(Widget):
    def __init__(self, card_holder: MultipleCardsHolder):
        super().__init__(QVBoxLayout())
        self.card_holder = card_holder

        # TODO styling
        # TODO -> extract sizes to a common location to keep this in-line with the card size.
        self.widget.setFixedSize(64, 104)
        self.widget.setObjectName("outline")
        self.style_with_selectors(
            {
                "*": {
                    "background-color": "#C0C0C0",
                },
                "#outline": {
                    "border-style": "dashed",
                    "border-radius": "5px",
                    "border-width": "2px",
                    "border-color": "blue"
                },
            }
        )
        size_lbl = QLabel(str(len(card_holder)))
        size_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_widgets(size_lbl)
