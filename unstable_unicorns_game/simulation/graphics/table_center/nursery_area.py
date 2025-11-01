""" nursery area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.nursery import Nursery
from unstable_unicorns_game.simulation.graphics.cards.card_pile import CardPileUi
from unstable_unicorns_game.simulation.graphics.utility import Widget
from unstable_unicorns_game.simulation.graphics.utility.widget import GROUP_STYLES


class NurseryArea(Widget):

    @classmethod
    def create_widget(cls, nursery: Nursery) -> QWidget:
        return cls(nursery).widget

    def __init__(self, nursery: Nursery):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(GROUP_STYLES["card_piles"])

        self.widget.setObjectName("container")

        lbl = QLabel("Nursery")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_pile = CardPileUi(nursery)
        self.add_widgets(lbl, card_pile.widget)

        self.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
