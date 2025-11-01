""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow, CardViewMode
from unstable_unicorns_game.simulation.graphics.widget import GROUP_STYLES
from unstable_unicorns_game.simulation.graphics.widget import Widget


class StableArea(Widget):
    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())

        self.view_mode = CardViewMode.EXPANDED

        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        self.label = QLabel("Stable")
        self.label.setObjectName("lbl")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.cards = CardsRow(stable.unicorns + stable.upgrades + stable.downgrades)
        self.add_widgets(self.label, self.cards.widget)

        self.layout.setAlignment(self.cards.widget, Qt.AlignmentFlag.AlignLeft)
