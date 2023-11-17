""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout

from simulation.graphics.card_box import CardBox
from simulation.graphics.utility import Widget


class UnicornCards(Widget):
    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("unicorn_cards")
        for _ in range(7):
            self.layout.addWidget(CardBox.create_widget())


class Unicorns(Widget):

    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.style_with_selectors({
            "*": {"background-color": "#f0f5c1"},
            "QLabel": {"background-color": "#e3f5c1"},
            "#unicorn_cards": {"background-color": "#c1f5c1"}
        })

        lbl = QLabel("Unicorns")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(lbl)

        self.layout.addWidget(UnicornCards.create_widget())


class GradesHands(Widget):
    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("cards")

        for _ in range(3):
            self.layout.addWidget(CardBox.create_widget())


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
        self.layout.addWidget(lbl)
        self.layout.addWidget(GradesHands.create_widget())


class StableArea(Widget):
    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())

        self.style_with_selectors({
            "*": {"background-color": "#f5c1c6"},
            "QLabel": {"background-color": "#f5cdc1"}
        })

        self.stable_lbl = QLabel("Stable")
        self.stable_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.stable_lbl)

        self.layout.addWidget(Unicorns.create_widget())
        self.layout.addWidget(GradesArea.create_widget())
