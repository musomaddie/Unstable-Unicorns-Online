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

    # TODO (NOTE) these now live at this level because they should only be used in the context of dealing with a list
    #  of things, and this is really the only place where we have this.
    def append_widget(self, widget: Widget):
        self.layout.addWidget(widget.widget)
        self.children.append(widget)

    def remove_child(self, child: Widget):
        child.widget.setParent(None)
        self.children.remove(child)

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

    def _add_missing_card_ui(self):
        ui_ids_list = [cui.card_id() for cui in self.cards_and_ui]
        for card in self.cards:
            if card.unique_id in ui_ids_list:
                continue
            new_ui = CardUi(card)
            self.append_widget(new_ui)
            self.cards_and_ui.append(CardToUi(card, new_ui))

    def _remove_card_ui(self):
        remaining_cards = [card.unique_id for card in self.cards]
        for cui in self.cards_and_ui:
            if cui.card_id() in remaining_cards:
                continue
            self.cards_and_ui.remove(cui)
            self.remove_child(cui.ui)

    def update(self):
        if len(self.cards_and_ui) == len(self.cards):
            # Displaying the correct number of cards, no further work.
            return
        if len(self.cards) > len(self.cards_and_ui):
            self._add_missing_card_ui()
        if len(self.cards) < len(self.cards_and_ui):
            self._remove_card_ui()
        pass


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

    def update(self):
        # TODO -> handle filter (and hiding when empty).
        self.label.update_text(str(len(self.cards)))


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

    def update(self):
        self._container_view.update()
