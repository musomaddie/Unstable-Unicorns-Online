""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel, QVBoxLayout

from simulation.graphics.card_box import CardBox
from simulation.graphics.utility import Widget


class Cards(Widget):

    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("hand")
        for _ in range(7):
            # TODO -> do this differently -> I actually want the cards themselves not just spaces.
            self.layout.addWidget(CardBox.create_widget())


class HandBoard(Widget):

    @classmethod
    def create_widget(cls, condensed: bool) -> QWidget:
        return cls(condensed).widget

    def __init__(self, condensed):
        super().__init__(QHBoxLayout() if condensed else QVBoxLayout())
        self.style_with_selectors(
            {
                "*": {"background-color": "#f5c1f1"},
                "QLabel": {"background-color": "#c7c1f5"},
                "#hand": {"background-color": "#e5c1f5"}
            }
        )

        # label
        lbl = QLabel("Hand")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(lbl)

        # cards
        self.layout.addWidget(Cards.create_widget())
