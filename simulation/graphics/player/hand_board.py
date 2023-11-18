""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel

from game_details.hand import Hand
from simulation.graphics.card_ui import CardUi, CardUiType
from simulation.graphics.utility import Widget


class Cards(Widget):

    @classmethod
    def create_widget(cls, hand: Hand) -> QWidget:
        return cls(hand).widget

    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("hand")
        # TODO -> do this differently -> I actually want the cards themselves not just spaces.
        self.add_widgets(
            *[
                CardUi.create_widget(CardUiType.from_card(card), card)
                for card in hand
            ]
        )


class HandBoard(Widget):

    @classmethod
    def create_widget(cls, hand: Hand) -> QWidget:
        return cls(hand).widget

    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        self.style_with_selectors(
            {
                "*": {"background-color": "#f5c1f1"},
                "QLabel": {"background-color": "#c7c1f5"},
                "#hand": {"background-color": "#e5c1f5"}
            }
        )

        lbl = QLabel("Hand")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(lbl, Cards.create_widget(hand))
