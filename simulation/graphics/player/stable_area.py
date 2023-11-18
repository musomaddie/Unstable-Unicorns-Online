""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout

from game_details.stable import Stable
from simulation.graphics.card_ui import CardUiType, CardUi
from simulation.graphics.utility import Widget


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

        self.style_with_selectors({
            "*": {"background-color": "#f5c1c6"},
            "QLabel": {"background-color": "#f5cdc1"},
            "#cards": {"background-color": "#a2f1fa"}
        })

        self.stable_lbl = QLabel("Stable")
        self.stable_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(
            self.stable_lbl,
            StableCards.create_widget(stable))
