""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


class CardPileUi(ContainerWidget):
    def __init__(self, card_holder: MultipleCardsHolder):
        super().__init__(QVBoxLayout())
        self.card_holder = card_holder

        # TODO styling (and maybe make modifable??)
        self.widget.setFixedSize(styles.CARD_WIDTH, styles.CARD_HEIGHT)
        self.widget.setObjectName("outline")
        self.style_with_selectors(styles.table_center_card_piles)
        size_lbl = CenteredLabel(str(len(card_holder)))
        self.add_widgets(size_lbl)
