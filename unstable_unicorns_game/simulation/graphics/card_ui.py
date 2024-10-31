""" Card ui. """
from dataclasses import dataclass
from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel

from unstable_unicorns_game.game_details.card import Card, CardType
from unstable_unicorns_game.simulation.graphics.utility import Widget


@dataclass
class CardTypeData:
    """ Associated data for each Card Type"""
    svg_name: str = ""
    include_text: bool = True


class CardUiType(Enum):
    """ Different possible types of cards."""
    BABY_UNICORN = CardTypeData(svg_name="baby_unicorn")
    BABY_HOLDER = CardTypeData(svg_name="baby_unicorn", include_text=False)
    BASIC_UNICORN = CardTypeData(svg_name="basic_unicorn")
    BLANK = CardTypeData(include_text=False)
    DOWNGRADE = CardTypeData(svg_name="downgrade")
    INSTANT = CardTypeData(svg_name="instant")
    MAGIC = CardTypeData(svg_name="magic")
    MAGIC_UNICORN = CardTypeData(svg_name="magic_unicorn")
    UNKNOWN = CardTypeData(svg_name="unknown", include_text=False)
    UPGRADE = CardTypeData(svg_name="upgrade")

    @staticmethod
    def from_card(card: Card) -> 'CardUiType':
        """ Returns the corresponding type from the given card. """
        if card.card_type == CardType.BABY_UNICORN:
            return CardUiType.BABY_UNICORN
        if card.card_type == CardType.BASIC_UNICORN:
            return CardUiType.BASIC_UNICORN
        if card.card_type == CardType.DOWNGRADE:
            return CardUiType.DOWNGRADE
        if card.card_type == CardType.INSTANT:
            return CardUiType.INSTANT
        if card.card_type == CardType.MAGIC:
            return CardUiType.MAGIC
        if card.card_type == CardType.MAGIC_UNICORN:
            return CardUiType.MAGIC_UNICORN
        if card.card_type == CardType.UPGRADE:
            return CardUiType.UPGRADE
        return CardUiType.UNKNOWN


class CardUi(Widget):
    @classmethod
    def create_widget(cls, card_type: CardUiType, card: Card = None) -> QWidget:
        return cls(card_type, card).widget

    def __init__(self, card_type: CardUiType, card: Card = None):
        super().__init__(QVBoxLayout())

        # TODO - reconsider this based on other cards.
        self.widget.setFixedSize(64, 104)
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
        if card_type != CardUiType.BLANK:
            image = QPixmap(f"simulation/graphics/images/card_types/{card_type.value.svg_name}.svg")
            label = QLabel()
            label.setPixmap(image)
            self.add_widgets(label)
            # If there's text add it
            if card_type.value.include_text and card is not None:
                name_lbl = QLabel(card.name)
                name_lbl.setWordWrap(True)
                name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.add_widgets(name_lbl)
