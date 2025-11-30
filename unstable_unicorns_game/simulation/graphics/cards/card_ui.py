""" Card ui. """
from dataclasses import dataclass
from enum import Enum

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.utility.measurements import CARD_SIZE
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.image import Image
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


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


class CardUi(ContainerWidget):
    def __init__(self, card: Card):
        super().__init__(QVBoxLayout(), style_identifier="outline", styling=styles.single_card(), size=CARD_SIZE)

        card_type = CardUiType.from_card(card)

        if card_type != CardUiType.BLANK:
            image = Image(f"simulation/graphics/images/card_types/{card_type.value.svg_name}.svg")
            self.add_widgets(image)
            # If there's text add it
            if card_type.value.include_text and card is not None:
                name_lbl = CenteredLabel(card.name, word_wrap=True)
                self.add_widgets(name_lbl)

        self.disable_card_selection()

    def enable_card_selection(self, on_click):
        self.widget.mousePressEvent = on_click

    def disable_card_selection(self):
        self.widget.mousePressEvent = None
