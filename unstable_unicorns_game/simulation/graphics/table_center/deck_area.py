""" deck area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.simulation.graphics.cards.card_pile import CardPileUi
from unstable_unicorns_game.simulation.graphics.utility import Widget
from unstable_unicorns_game.simulation.graphics.utility.widget import GROUP_STYLES


class DeckArea(Widget):

    @classmethod
    def create_widget(cls, deck: Deck) -> QWidget:
        return cls(deck).widget

    def __init__(self, deck: Deck):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(
            GROUP_STYLES["card_piles"])

        self.widget.setObjectName("container")

        lbl = QLabel("Deck")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_pile = CardPileUi(deck)
        self.add_widgets(lbl, card_pile.widget)

        self.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
