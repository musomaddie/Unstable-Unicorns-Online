""" discard area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.simulation.graphics.cards.card_pile import CardPileUi
from unstable_unicorns_game.simulation.graphics.utility import Widget
from unstable_unicorns_game.simulation.graphics.utility.widget import GROUP_STYLES


class DiscardArea(Widget):

    @classmethod
    def create_widget(cls, discard: DiscardPile) -> QWidget:
        return cls(discard).widget

    def __init__(self, discard: DiscardPile):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(GROUP_STYLES["card_piles"])
        self.widget.setObjectName("container")

        lbl = QLabel("Discard Pile")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_space = CardPileUi(discard)

        self.add_widgets(lbl, card_space.widget)
        self.layout.setAlignment(card_space.widget, Qt.AlignmentFlag.AlignCenter)
