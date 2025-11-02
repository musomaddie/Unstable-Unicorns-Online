""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.utility.colours import GREY
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import CARD_HEIGHT, CARD_WIDTH, ContainerWidget


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
        size_lbl = CenteredLabel(str(len(card_holder)))
        self.add_widgets(size_lbl)
