from dataclasses import dataclass
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

import unstable_unicorns_game.gui.resources.measurement as measurements
import unstable_unicorns_game.gui.resources.style as styles
from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.gui.cards.card_ui import CardUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


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


class CardsPileView(CardsView):
    label: Label

    def __init__(self, cards: MultipleCardsHolder, **kwargs):
        self.label = Label(
            str(len(cards)),
            alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter,
        )
        super().__init__(
            cards,
            layout=QVBoxLayout(),
            children=[self.label],
            styling=styles.card_piles(),
            style_identifier="outline",
            size=measurements.CARD_SIZE,
            **kwargs)


class CardsContainerWithUi:
    cards: MultipleCardsHolder
    _container_view: CardsView
    overall_view: ContainerWidget

    def __init__(
            self,
            cards: MultipleCardsHolder,
            label: Label,
            container_view: CardsView,
            overall_view: ContainerWidget):
        self.cards = cards
        self._container_view = container_view
        self.overall_view = overall_view

        self.overall_view.add_widgets(label, self._container_view)
