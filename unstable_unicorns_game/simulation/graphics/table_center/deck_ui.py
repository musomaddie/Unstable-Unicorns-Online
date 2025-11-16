""" deck area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardsContainerUi, CardsPile
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


class DeckUi:
    deck: Deck

    view: CardsContainerUi

    def __init__(self, deck: Deck):
        self.deck = deck
        pile = CardsPile(deck, styles.table_center_card_piles(), style_identifier="outline")
        self.view = CardsContainerUi(
            pile, CenteredLabel("Deck"),
            layout=QVBoxLayout(),
            style_identifier="container"
        )
        self.view.style_with_selectors(styles.table_center_card_piles_wrapper())

        self.view.align(Qt.AlignmentFlag.AlignCenter)
