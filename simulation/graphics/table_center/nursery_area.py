""" nursery area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from simulation.graphics.card_ui import CardUi, CardUiType
from simulation.graphics.utility import Widget
from simulation.graphics.utility.widget import GROUP_STYLES


class NurseryArea(Widget):

    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(GROUP_STYLES["card_piles"])

        self.widget.setObjectName("container")

        lbl = QLabel("Nursery")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_pile = CardUi(CardUiType.BABY_HOLDER)
        self.add_widgets(lbl, card_pile.widget)

        self.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
