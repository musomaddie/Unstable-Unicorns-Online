""" discard area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.simulation.graphics.cards.card_pile import CardPileUi
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widget.widget import GROUP_STYLES


class DiscardArea(ContainerWidget):

    def __init__(self, discard: DiscardPile):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(GROUP_STYLES["card_piles"])
        self.widget.setObjectName("container")

        lbl = QLabel("Discard Pile")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_space = CardPileUi(discard)

        self.add_qwidget(lbl)
        self.add_widgets(card_space)
        self.layout.setAlignment(card_space.widget, Qt.AlignmentFlag.AlignCenter)
