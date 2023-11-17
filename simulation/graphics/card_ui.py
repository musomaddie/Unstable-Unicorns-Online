""" Card ui. """
from dataclasses import dataclass
from enum import Enum

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel

from simulation.graphics.utility import Widget


@dataclass
class CardTypeData:
    """ Associated data for each Card Type"""
    svg_name: str = ""


class CardUiType(Enum):
    """ Different possible types of cards."""
    BABY_UNICORN = CardTypeData(svg_name="baby_unicorn")
    BABY_HOLDER = CardTypeData(svg_name="baby_unicorn")
    BASIC_UNICORN = CardTypeData(svg_name="basic_unicorn")
    BLANK = CardTypeData()
    DOWNGRADE = CardTypeData(svg_name="downgrade")
    INSTANT = CardTypeData(svg_name="instant")
    MAGIC = CardTypeData(svg_name="magic")
    MAGIC_UNICORN = CardTypeData(svg_name="magic_unicorn")
    UNKNOWN = CardTypeData(svg_name="unknown")
    UPGRADE = CardTypeData(svg_name="upgrade")


class CardUi(Widget):
    @classmethod
    def create_widget(cls, card_type: CardUiType) -> QWidget:
        return cls(card_type).widget

    def __init__(self, card_type: CardUiType):
        super().__init__(QVBoxLayout())

        self.widget.setFixedSize(64, 104)  # a golden rectangle.
        self.widget.setObjectName("outline")
        self.style_with_selectors(
            {
                "*": {
                    "background-color": "#C0C0C0",
                },
                "#outline": {
                    "border-style": "dashed",
                    "border-radius": "5px",
                    "border-width": "2px",
                    "border-color": "black"
                },
            })
        if card_type != card_type.BLANK:
            image = QPixmap(f"simulation/graphics/images/card_types/{card_type.value.svg_name}.svg")
            label = QLabel()
            label.setPixmap(image)
            self.add_widgets(label)
