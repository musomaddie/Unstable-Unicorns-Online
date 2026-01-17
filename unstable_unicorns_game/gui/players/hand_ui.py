from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsPileView, CardsRowView
from unstable_unicorns_game.gui.resources import alignment, style
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


def create_compact_container(hand: Hand) -> CardsContainerWithUi:
    lbl = Label("H:", alignment=alignment.right(), horizontal_stretch=1)
    cards_view = CardsPileView(hand.cards, custom_styling=style.compact_card_pile())
    return CardsContainerWithUi(
        hand.cards,
        label=lbl,
        container_view=cards_view,
        overall_view=ContainerWidget(QHBoxLayout(), style_identifier="container"),
        custom_children=[lbl, ContainerWidget(QHBoxLayout(), children=[cards_view], horizontal_stretch=3)])


class HandUi:
    """ The UI for a player's hand. """
    hand: Hand
    container: CardsContainerWithUi
    compact_container: CardsContainerWithUi
    detailed_container: CardsContainerWithUi

    view: ContainerWidget
    compact_view: ContainerWidget
    detailed_view: ContainerWidget

    def __init__(self, hand: Hand):
        self.hand = hand
        self.container = CardsContainerWithUi(
            hand.cards,
            label=Label("Hand", alignment=alignment.right(), horizontal_stretch=1),
            container_view=CardsRowView(hand.cards, horizontal_stretch=3),
            overall_view=ContainerWidget(
                QHBoxLayout(), style_identifier="container", margins=Margins(top=10, bottom=10), ))
        self.compact_container = create_compact_container(hand)
        self.detailed_container = CardsContainerWithUi(
            hand.cards,
            label=Label("Hand", alignment=alignment.right(), horizontal_stretch=1),
            container_view=CardsRowView(hand.cards, horizontal_stretch=3),
            overall_view=ContainerWidget(
                QHBoxLayout(), style_identifier="container", margins=Margins(top=5, bottom=5)))

        self.view = self.container.overall_view
        self.compact_view = self.compact_container.overall_view
        self.detailed_view = self.detailed_container.overall_view

    def update(self):
        self.container.update()
        self.compact_container.update()
        self.detailed_container.update()

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        self.container.enable_card_selection(on_click)
        self.compact_container.enable_card_selection(on_click)
        self.detailed_container.enable_card_selection(on_click)

    def disable_card_selection(self):
        self.container.disable_card_selection()
        self.compact_container.disable_card_selection()
        self.detailed_container.disable_card_selection()
