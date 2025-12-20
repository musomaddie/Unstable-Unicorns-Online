from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

import unstable_unicorns_game.gui.resources.style as styles
from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsPileView
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class DeckUi:
    deck: Deck
    cards_container: CardsContainerWithUi
    view: ContainerWidget

    def __init__(self, deck: Deck):
        self.deck = deck
        self.cards_container = CardsContainerWithUi(
            deck,
            label=Label(
                "Deck", alignment=Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter, ),
            container_view=CardsPileView(deck),
            overall_view=ContainerWidget(
                layout=QVBoxLayout(), style_identifier="container", styling=styles.table_center_pile_wrapper(), ))
        self.view = self.cards_container.overall_view
