""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout

from game_details.card import MultipleCardsHolder
from game_details.stable import Stable
from simulation.graphics.card_box import CardBox
from simulation.graphics.card_ui import CardUiType, CardUi
from simulation.graphics.utility import Widget


class UnicornCards(Widget):
    @classmethod
    def create_widget(cls, unicorns: MultipleCardsHolder) -> QWidget:
        return cls(unicorns).widget

    def __init__(self, unicorns: MultipleCardsHolder):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("unicorn_cards")
        self.add_widgets(
            *[
                CardUi.create_widget(CardUiType.from_card(card), card)
                for card in unicorns
            ]
        )


class Unicorns(Widget):

    @classmethod
    def create_widget(cls, unicorns: MultipleCardsHolder) -> QWidget:
        return cls(unicorns).widget

    def __init__(self, unicorns: MultipleCardsHolder):
        super().__init__(QHBoxLayout())
        self.style_with_selectors({
            "*": {"background-color": "#f0f5c1"},
            "QLabel": {"background-color": "#e3f5c1"},
            "#unicorn_cards": {"background-color": "#c1f5c1"}
        })

        lbl = QLabel("Unicorns")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(lbl, UnicornCards.create_widget(unicorns))


class GradesHands(Widget):
    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("cards")

        self.add_widgets(*[CardBox.create_widget() for _ in range(3)])


class GradesArea(Widget):

    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.style_with_selectors({
            "*": {"background-color": "#a2fabd"},
            "QLabel": {"background-color": "#a2fae7"},
            "#cards": {"background-color": "#a2f1fa"}
        })

        lbl = QLabel("Upgrades / Downgrades")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(lbl, GradesHands.create_widget())


class StableArea(Widget):
    @classmethod
    def create_widget(cls, stable: Stable) -> QWidget:
        return cls(stable).widget

    def __init__(self, stable: Stable):
        super().__init__(QVBoxLayout())

        self.style_with_selectors({
            "*": {"background-color": "#f5c1c6"},
            "QLabel": {"background-color": "#f5cdc1"}
        })

        self.stable_lbl = QLabel("Stable")
        self.stable_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.add_widgets(self.stable_lbl, Unicorns.create_widget(stable.unicorns), GradesArea.create_widget())
