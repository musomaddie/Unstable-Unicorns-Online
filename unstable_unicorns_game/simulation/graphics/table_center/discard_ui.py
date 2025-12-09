""" discard area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardsContainerUi, CardsPile
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


class DiscardUi:
    # TODO -> this can be merged with deck into something like a "CenterCardPile" that they all can implement.
    discard: DiscardPile
    view: CardsContainerUi

    def __init__(self, discard: DiscardPile):
        self.discard = discard
        pile = CardsPile(discard, styles.table_center_card_piles(), style_identifier="outline")
        self.view = CardsContainerUi(
            pile, CenteredLabel("Discard"), layout=QVBoxLayout(), style_identifier="container",
            styling=styles.table_center_card_piles_wrapper(), align=Qt.AlignmentFlag.AlignCenter)

    def update(self):
        self.view.cards_container.update()
