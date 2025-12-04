""" discard area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.simulation.graphics.cards.card_pile import create_center_card_pile
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


class DiscardArea(ContainerWidget):

    def __init__(self, discard: DiscardPile):
        lbl = CenteredLabel("Discard Pile")
        card_space = create_center_card_pile(discard)

        super().__init__(
            QVBoxLayout(), style_identifier="container", styling=styles.table_center_card_piles_wrapper(),
            children=[lbl, card_space])
        self.widget.setObjectName("container")

        self.layout.setAlignment(card_space.widget, Qt.AlignmentFlag.AlignCenter)
