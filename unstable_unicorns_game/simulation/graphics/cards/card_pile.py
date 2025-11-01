""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel

from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.utility.colours import GREY
from unstable_unicorns_game.simulation.graphics.widget import ContainerWidget, CARD_WIDTH, CARD_HEIGHT


class CardPileUi(ContainerWidget):
    def __init__(self, card_holder: MultipleCardsHolder):
        super().__init__(QVBoxLayout())
        self.card_holder = card_holder

        # TODO styling
        self.widget.setFixedSize(CARD_WIDTH, CARD_HEIGHT)
        self.widget.setObjectName("outline")
        self.style_with_selectors(
            {
                "*": {
                    "background-color": GREY,
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
