""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel

from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.simulation.graphics.card_ui import CardUi, CardUiType
from unstable_unicorns_game.simulation.graphics.utility import Widget
from unstable_unicorns_game.simulation.graphics.utility.widget import GROUP_STYLES


class Cards(Widget):

    @classmethod
    def create_widget(cls, hand: Hand) -> QWidget:
        return cls(hand).widget

    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("hand")
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
        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        lbl = QLabel("Hand")
        lbl.setObjectName("lbl")
        lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        cards = Cards.create_widget(hand)

        self.add_widgets(lbl, cards)
        self.layout.setAlignment(cards, Qt.AlignmentFlag.AlignLeft)
