from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsPileView, CardsRowView
from unstable_unicorns_game.gui.resources import alignment
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class HandUi:
    """ The UI for a player's hand. """
    hand: Hand
    container: CardsContainerWithUi
    compact_container: CardsContainerWithUi

    view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, hand: Hand):
        self.hand = hand
        self.container = CardsContainerWithUi(
            hand,
            label=Label("Hand", alignment=alignment.right()),
            container_view=CardsRowView(hand),
            overall_view=ContainerWidget(
                QHBoxLayout(),
                style_identifier="container",
                margins=Margins(top=10, bottom=10)
            ))
        # TODO -> improve compact styling (at least a little).
        self.compact_container = CardsContainerWithUi(
            hand, label=Label("H:", alignment=alignment.right()),
            container_view=CardsPileView(hand),
            overall_view=ContainerWidget(QHBoxLayout(), style_identifier="container")
        )

        self.view = self.container.overall_view
        self.compact_view = self.compact_container.overall_view
