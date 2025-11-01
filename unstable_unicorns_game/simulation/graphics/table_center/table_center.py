""" layout for main board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_center.deck_area import DeckArea
from unstable_unicorns_game.simulation.graphics.table_center.discard_area import DiscardArea
from unstable_unicorns_game.simulation.graphics.table_center.nursery_area import NurseryArea
from unstable_unicorns_game.simulation.graphics.utility import Widget


class TableCenter(Widget):

    @classmethod
    def create_widget(cls, game: Game) -> QWidget:
        return cls(game).widget

    def __init__(self, game: Game):
        super().__init__(QHBoxLayout())
        self.style({
            "font-family": "Permanent Marker",
            "font-size": "20px",
        })
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_widgets(
            NurseryArea.create_widget(game.nursery),
            DeckArea.create_widget(game.deck),
            DiscardArea.create_widget(game.discard_pile)
        )
