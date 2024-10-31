""" discard area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from unstable_unicorns_game.simulation.graphics.card_ui import CardUi, CardUiType
from unstable_unicorns_game.simulation.graphics.utility import Widget
from unstable_unicorns_game.simulation.graphics.utility.widget import GROUP_STYLES


class DiscardArea(Widget):

    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.style_with_selectors(GROUP_STYLES["card_piles"])
        self.widget.setObjectName("container")

        lbl = QLabel("Discard Pile")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_space = CardUi(CardUiType.BLANK)

        self.add_widgets(lbl, card_space.widget)
        self.layout.setAlignment(card_space.widget, Qt.AlignmentFlag.AlignCenter)
