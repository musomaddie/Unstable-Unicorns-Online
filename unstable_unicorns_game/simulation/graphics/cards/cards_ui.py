from dataclasses import dataclass
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUi
from unstable_unicorns_game.simulation.graphics.utility.measurements import CARD_SIZE
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel, Label


def create_row_of_cards(cards: list[Card]) -> ContainerWidget:
    return ContainerWidget(
        QHBoxLayout(), style_identifier="cards-row",
        chidlren=[CardUi(card) for card in cards])


@dataclass
class CardToUi:
    card: Card
    ui: CardUi

    def card_id(self):
        return self.card.unique_id

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        self.ui.enable_card_selection(lambda _: on_click(self.card))

    def disable_card_selection(self):
        self.ui.disable_card_selection()


class CardsGroupWithUi(ContainerWidget):
    cards_callable: Callable[[], list[Card]]
    cards: list[Card]
    label: CenteredLabel

    def __init__(self, cards_callable: Callable[[], list[Card]], **kwargs):
        self.card_callable = cards_callable
        self.cards = cards_callable()
        self.label = CenteredLabel(str(len(self.cards)))

        super().__init__(
            QVBoxLayout(), style_identifier="container", size=CARD_SIZE, children=[self.label],
            **kwargs)


# TODO -> mark this is an abstract class.
class CardsContainer(ContainerWidget):
    holder: MultipleCardsHolder

    def __init__(self, holder: MultipleCardsHolder, layout: QLayout, **kwargs):
        self.holder = holder
        super().__init__(layout, **kwargs)

    def update(self):
        pass

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        pass

    def disable_card_selection(self):
        pass


class CardsRow(CardsContainer):
    cards_and_ui: list[CardToUi]

    def __init__(self, holder: MultipleCardsHolder, **kwargs):
        self.cards_and_ui = [CardToUi(card, CardUi(card)) for card in holder.cards]
        super().__init__(
            holder, layout=QHBoxLayout(), style_identifier="cards-row",
            children=[cu.ui for cu in self.cards_and_ui],
            **kwargs)

    def _add_missing_card_ui(self):
        ui_ids_list = [card_ui.card_id() for card_ui in self.cards_and_ui]
        for card in self.holder.cards:
            if card.unique_id in ui_ids_list:
                continue
            new_card_ui = CardUi(card)
            self.append_widget(new_card_ui)
            self.cards_and_ui.append(CardToUi(card, new_card_ui))

    def update(self):
        if len(self.cards_and_ui) == len(self.holder.cards):
            # There's the correct number of cards, so there's nothing to do.
            return
        if len(self.holder.cards) > len(self.cards_and_ui):
            self._add_missing_card_ui()

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        for card in self.cards_and_ui:
            card.enable_card_selection(on_click)

    def disable_card_selection(self):
        for card in self.cards_and_ui:
            card.disable_card_selection()


class CardsPile(CardsContainer):
    label: CenteredLabel

    def __init__(
            self, holder: MultipleCardsHolder, styling: dict[str, dict[str, str]] = None, **kwargs):
        self.label = CenteredLabel(str(len(holder.cards)))
        super().__init__(
            holder, layout=QVBoxLayout(), size=CARD_SIZE,
            children=[self.label],
            **kwargs)

        if styling:
            self.style_selectors(styling)

    def update(self):
        self.label.label.setText(str(len(self.holder.cards)))


class CardsContainerUi(ContainerWidget):
    cards_container: CardsContainer
    label: Label

    def __init__(self, cards_container: CardsContainer, label: Label, layout: QLayout, **kwargs):
        self.cards_container = cards_container
        self.label = label
        super().__init__(layout, children=[label, cards_container], **kwargs)
