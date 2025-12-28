from dataclasses import dataclass
from typing import Callable, Optional

from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.gui.cards.card_ui import CardUi
from unstable_unicorns_game.gui.resources import alignment, measurement, style
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label
from unstable_unicorns_game.gui.widgets.widget import Widget


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
    cards: list[Card]

    def __init__(self, cards: list[Card], layout: QLayout, **kwargs):
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

    def __init__(self, cards: list[Card], **kwargs):
        self.cards_and_ui = [CardToUi(card, CardUi(card)) for card in cards]
        super().__init__(
            cards, layout=QHBoxLayout(), children=[cui.ui for cui in self.cards_and_ui], spacing=10, **kwargs)


class CardsPileView(CardsView):
    label: Label
    filter: Optional[Callable[[], list[Card]]]
    hide_when_empty: bool

    def __init__(
            self,
            cards: list[Card],
            cards_filter: Optional[Callable[[], list[Card]]] = None,
            custom_styling: Optional[dict[str, dict[str, str]]] = None,
            hide_when_empty: bool = False,
            **kwargs):
        self.hide_when_empty = hide_when_empty
        self.filter = cards_filter
        if self.filter:
            cards = self.filter()

        self.label = Label(str(len(cards)), alignment=alignment.center())

        super().__init__(
            cards,
            layout=QVBoxLayout(),
            children=[self.label],
            style_identifier="outline",
            styling=custom_styling if custom_styling else style.card_piles(),
            size=measurement.CARD_SIZE,
            **kwargs)

        if self.hide_when_empty and len(self.cards) == 0:
            self.hide()


class CardsContainerWithUi:
    cards: list[Card]
    _container_view: CardsView
    overall_view: ContainerWidget

    def __init__(
            self,
            cards: list[Card],
            label: Label,
            container_view: CardsView,
            overall_view: ContainerWidget,
            custom_children: Optional[list[Widget]] = None):
        self.cards = cards
        self._container_view = container_view
        self.overall_view = overall_view

        if custom_children:
            self.overall_view.add_widgets(*custom_children)
        else:
            self.overall_view.add_widgets(label, self._container_view)
