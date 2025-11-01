""" player hand board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel

from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow
from unstable_unicorns_game.simulation.graphics.widget import GROUP_STYLES, Widget


#
# class Cards(Widget):
#     def __init__(self, hand: Hand):
#         super().__init__(QHBoxLayout())
#         self.widget.setObjectName("hand")
#         self.add_widgets(
#             *[
#                 CardUi(CardUiType.from_card(card), card).widget
#                 for card in hand
#             ]
#         )
#

class HandBoard(Widget):
    def __init__(self, hand: Hand):
        super().__init__(QHBoxLayout())
        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        self.label = QLabel("Hand")
        self.label.setObjectName("lbl")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.cards = CardsRow(hand.cards)

        self.add_widgets(self.label, self.cards.widget)
        self.layout.setAlignment(self.cards.widget, Qt.AlignmentFlag.AlignLeft)
