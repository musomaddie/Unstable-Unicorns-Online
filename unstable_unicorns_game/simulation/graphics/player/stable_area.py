""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.cards import CardViewMode, CardsRow
from unstable_unicorns_game.simulation.graphics.widget.label import RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget, GROUP_STYLES


class StableArea(ContainerWidget):
    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())

        self.view_mode = CardViewMode.EXPANDED

        self.style_with_selectors(GROUP_STYLES["player_board_labels"])
        self.label = RightAlignedLabel("Stable", style_identifier="lbl")

        self.cards = CardsRow(stable.unicorns + stable.upgrades + stable.downgrades)
        self.add_widgets(self.label, self.cards)

        self.layout.setAlignment(self.cards.widget, Qt.AlignmentFlag.AlignLeft)
