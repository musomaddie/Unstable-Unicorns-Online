from dataclasses import dataclass
from enum import Enum

from PyQt6.QtWidgets import QLabel, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.image import Image
from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget


# TODO -> restructure to use a mixin like in pymusic.
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
        match card.card_type:
            case CardType.BABY_UNICORN:
                return CardUiType.BABY_UNICORN
            case CardType.BASIC_UNICORN:
                return CardUiType.BASIC_UNICORN
            case CardType.DOWNGRADE:
                return CardUiType.DOWNGRADE
            case CardType.INSTANT:
                return CardUiType.INSTANT
            case CardType.MAGIC:
                return CardUiType.MAGIC
            case CardType.MAGIC_UNICORN:
                return CardUiType.MAGIC_UNICORN
            case CardType.UPGRADE:
                return CardUiType.UPGRADE


class CardUi(ContainerWidget):
    def __init__(self, card: Card):
        # TODO -> copy styling.
        super().__init__(QVBoxLayout())

        card_type = CardUiType.from_card(card)
        if card_type != CardUiType.BLANK:
            # TODO -> make the image actually work
            image = Image(f"gui/resources/images/card_types/{card_type.value.svg_name}.svg")
            self.add_widgets(image)
            if card_type.value.include_text and card is not None:
                # TODO -> style and word wrap.
                name_lbl = QLabel(card.name)
                self.add_widgets(Widget(name_lbl))

    def enable_click(self, on_click):
        self.widget.mousePressEvent = on_click

    def disable_click(self):
        self.widget.mousePressEvent = None
