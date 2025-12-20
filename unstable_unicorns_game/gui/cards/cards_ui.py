from dataclasses import dataclass
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.gui.cards.card_ui import CardUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


@dataclass
class CardToUi:
    card: Card
    ui: CardUi

    def card_id(self):
        return self.card.unique_id

    def enable_click(self, on_click: Callable[[Card], None]):
        self.ui.enable_click(on_click)

    def disable_click(self):
        self.ui.disable_click()


class CardsView(ContainerWidget):
    cards: MultipleCardsHolder

    def __init__(self, cards: MultipleCardsHolder, layout: QLayout, **kwargs):
        self.cards = cards
        super().__init__(layout, **kwargs)

    def update(self):
        pass

    def enable_click(self, on_click: Callable[[Card], None]):
        pass

    def disable_click(self):
        pass


class CardsRowView(CardsView):
    cards_and_ui: list[CardToUi]

    def __init__(self, cards: MultipleCardsHolder, **kwargs):
        self.cards_and_ui = [CardToUi(card, CardUi(card)) for card in cards]
        super().__init__(cards, layout=QHBoxLayout(), **kwargs)


class CardsContainerWithUi:
    cards: MultipleCardsHolder
    # label: Label

    # view: ContainerWidget
