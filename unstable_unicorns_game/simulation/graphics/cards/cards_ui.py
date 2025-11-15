from dataclasses import dataclass

from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUi
from unstable_unicorns_game.simulation.graphics.utility import colours, styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel, Label
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def create_row_of_cards(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout(), style_identifier="cards-row")
    widget.add_widgets(
        *[CardUi(card) for card in cards]
    )

    return widget


@dataclass
class CardToUi:
    card: Card
    ui: CardUi


class CardsContainer(ContainerWidget):
    holder: MultipleCardsHolder

    def __init__(self, holder: MultipleCardsHolder, layout: QLayout, **kwargs):
        self.holder = holder
        super().__init__(layout, **kwargs)

    def update(self):
        print("Hello")
        print(self)


class CardsRow(CardsContainer):
    cards_and_ui: list[CardToUi]

    def __init__(self, holder: MultipleCardsHolder, **kwargs):
        super().__init__(holder, layout=QHBoxLayout(), style_identifier="cards-row", **kwargs)
        self.cards_and_ui = [CardToUi(card, CardUi(card)) for card in holder.cards]
        self.add_widgets(*[cu.ui for cu in self.cards_and_ui])

    def _make_missing_card_ui(self):
        print(self.cards_and_ui)
        for card in self.holder.cards:
            print(card)

    def update(self):
        # Check if a card should be added
        if len(self.holder.cards) > len(self.cards_and_ui):
            self._make_missing_card_ui()
            # Updating a row

            print("Updating a row")


class CardsPile(CardsContainer):

    def __init__(self, holder: MultipleCardsHolder, color: str = colours.grey, **kwargs):
        # TODO -> update style identifier based on pile location (player vs center)
        super().__init__(holder, layout=QVBoxLayout(), style_identifier="container", **kwargs)

        self.set_size(styles.CARD_WIDTH, styles.CARD_HEIGHT)
        self.style_with_selectors(styles.compact_card_pile_player(color))

        self.add_widgets(CenteredLabel(str(len(holder.cards))))


class CardsContainerUi(ContainerWidget):
    cards_container: CardsContainer
    label: Label

    def __init__(self, cards_container: CardsContainer, label: Label, layout: QLayout, **kwargs):
        self.cards_container = cards_container
        self.label = label
        super().__init__(layout, **kwargs)

        self.add_widgets(label, cards_container)
