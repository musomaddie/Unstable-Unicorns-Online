""" nursery area """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.nursery import Nursery
from unstable_unicorns_game.simulation.graphics.cards.card_pile import create_center_card_pile
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


class NurseryArea(ContainerWidget):

    def __init__(self, nursery: Nursery):
        super().__init__(QVBoxLayout(), style_identifier="container", styling=styles.table_center_card_piles_wrapper())

        self.widget.setObjectName("container")

        self.label = CenteredLabel("Nursery")
        card_pile = create_center_card_pile(nursery)
        self.add_widgets(self.label, card_pile)

        self.layout.setAlignment(card_pile.widget, Qt.AlignmentFlag.AlignCenter)
