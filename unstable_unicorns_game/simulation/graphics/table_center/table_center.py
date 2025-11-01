""" layout for main board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_center.deck_area import DeckArea
from unstable_unicorns_game.simulation.graphics.table_center.discard_area import DiscardArea
from unstable_unicorns_game.simulation.graphics.table_center.nursery_area import NurseryArea
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


class TableCenter(ContainerWidget):

    def __init__(self, game: Game):
        super().__init__(QHBoxLayout())
        self.style({
            # "font-family": "Permanent Marker",
            "font-size": "20px",
        })
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_widgets(
            NurseryArea(game.nursery),
            DeckArea(game.deck),
            DiscardArea(game.discard_pile)
        )
