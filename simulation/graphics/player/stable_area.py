""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

from game_details.stable import Stable
from simulation.graphics.card_ui import CardUiType, CardUi
from simulation.graphics.utility import Widget
from simulation.graphics.utility.widget import GROUP_STYLES


class StableCards(Widget):
    @classmethod
    def create_widget(cls, stable: Stable) -> QWidget:
        return cls(stable).widget

    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("cards")
        self.add_widgets(
            *[
                CardUi.create_widget(CardUiType.from_card(card), card)
                for card in stable.unicorns + stable.upgrades + stable.downgrades
            ]
        )


class StableArea(Widget):
    @classmethod
    def create_widget(cls, stable: Stable) -> QWidget:
        return cls(stable).widget

    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())

        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        stable_lbl = QLabel("Stable")
        stable_lbl.setObjectName("lbl")
        stable_lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        cards = StableCards.create_widget(stable)
        self.add_widgets(stable_lbl, cards)

        self.layout.setAlignment(cards, Qt.AlignmentFlag.AlignLeft)
