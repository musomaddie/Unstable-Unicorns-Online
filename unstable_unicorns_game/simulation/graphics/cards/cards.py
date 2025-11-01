from enum import Enum, auto

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUi
from unstable_unicorns_game.simulation.graphics.widget import ContainerWidget


class CardViewMode(Enum):
    """ How the cards should be displayed. Used all the way up to "card area". """
    EXPANDED = auto()
    COMPACT = auto()


class CardsRow(ContainerWidget):
    def __init__(self, cards: list[Card]):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("cards")
        self.card_uis = [
            CardUi(card)
            for card in cards
        ]

        self.add_widgets(*self.card_uis)
