""" deck area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from simulation.graphics.card_ui import CardUi, CardUiType
from simulation.graphics.utility import Widget
from simulation.graphics.utility.widget import GROUP_STYLES


class DeckArea(Widget):

    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(
            GROUP_STYLES["card_piles"])

        self.widget.setObjectName("container")

        lbl = QLabel("Deck")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_pile = CardUi.create_widget(CardUiType.UNKNOWN)
        self.add_widgets(lbl, card_pile)

        self.layout.setAlignment(card_pile, Qt.AlignmentFlag.AlignCenter)
