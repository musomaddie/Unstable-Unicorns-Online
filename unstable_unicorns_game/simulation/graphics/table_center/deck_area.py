""" deck area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.simulation.graphics.cards.card_pile import CardPileUi
from unstable_unicorns_game.simulation.graphics.widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widget import GROUP_STYLES


class DeckArea(ContainerWidget):
    def __init__(self, deck: Deck):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(
            GROUP_STYLES["card_piles"])

        self.widget.setObjectName("container")

        lbl = QLabel("Deck")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_pile = CardPileUi(deck)
        self.add_qwidget(lbl)
        self.add_widgets(card_pile)

        self.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
