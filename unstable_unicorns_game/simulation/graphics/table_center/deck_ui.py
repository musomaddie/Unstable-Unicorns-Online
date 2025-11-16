""" deck area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.simulation.graphics.cards.card_pile import create_center_card_pile
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


class DeckUi:
    deck: Deck

    pile_view: ContainerWidget

    def __init__(self, deck: Deck):
        self.deck = deck
        self.pile_view = ContainerWidget(QVBoxLayout(), style_identifier="container")
        self.pile_view.style_with_selectors(styles.table_center_card_piles_wrapper())

        lbl = CenteredLabel("Deck")
        card_pile = create_center_card_pile(deck)

        self.pile_view.add_widgets(lbl, card_pile)
        self.pile_view.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
