from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsPileView, CardsRowView
from unstable_unicorns_game.gui.resources import alignment, color, style
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


def create_filter(cards: list[Card], card_type: CardType) -> Callable[[], list[Card]]:
    return lambda: list(filter(lambda card: card.card_type == card_type, cards))


class CompactStableCards:
    baby_unicorns: CardsPileView
    basic_unicorns: CardsPileView
    magic_unicorns: CardsPileView

    view: ContainerWidget

    def __init__(self, stable: Stable):
        self.baby_unicorns = CardsPileView(
            stable.unicorns.cards,
            create_filter(stable.unicorns.cards, CardType.BABY_UNICORN),
            style.compact_card_pile(color.baby_unicorn_pink),
            hide_when_empty=True)
        self.basic_unicorns = CardsPileView(
            stable.unicorns.cards,
            create_filter(stable.unicorns.cards, CardType.BASIC_UNICORN),
            style.compact_card_pile(color.basic_unicorn_purple),
            hide_when_empty=True)
        self.magic_unicorns = CardsPileView(
            stable.unicorns.cards,
            create_filter(stable.unicorns.cards, CardType.MAGIC_UNICORN),
            style.compact_card_pile(color.magic_unicorn_blue),
            hide_when_empty=True)

        self.view = ContainerWidget(
            QHBoxLayout(),
            children=[self.baby_unicorns, self.basic_unicorns, self.magic_unicorns],
            horizontal_stretch=3)


class StableUi:
    stable: Stable

    container: CardsContainerWithUi
    compact_cards: CompactStableCards
    detailed_cards: CardsContainerWithUi

    view: ContainerWidget
    compact_view: ContainerWidget
    detailed_view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable

        stable_cards = stable.unicorns.cards + stable.upgrades.cards + stable.downgrades.cards

        self.container = CardsContainerWithUi(
            stable_cards,
            label=Label("Stable", alignment=alignment.right(), horizontal_stretch=1),
            container_view=CardsRowView(stable_cards, horizontal_stretch=5),
            overall_view=ContainerWidget(
                QHBoxLayout(), style_identifier="container", margins=Margins(top=10, bottom=10), vertical_stretch=3))
        self.view = self.container.overall_view

        self.compact_cards = CompactStableCards(stable)
        self.compact_view = ContainerWidget(
            QHBoxLayout(),
            children=[
                Label("S:", alignment=alignment.right(), horizontal_stretch=1), self.compact_cards.view],
            style_identifier="container")

        self.detailed_cards = CardsContainerWithUi(
            stable_cards,
            label=Label("Stable", alignment=alignment.right(), horizontal_stretch=1),
            container_view=CardsRowView(stable_cards, horizontal_stretch=3),
            overall_view=ContainerWidget(QHBoxLayout(), style_identifier="container", margins=Margins(top=5, bottom=5)))
        self.detailed_view = self.detailed_cards.overall_view
