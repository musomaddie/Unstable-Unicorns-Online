""" layout for main board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_center.deck_ui import DeckUi
from unstable_unicorns_game.simulation.graphics.table_center.discard_area import DiscardArea
from unstable_unicorns_game.simulation.graphics.table_center.nursery_area import NurseryArea
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget


class TableCenterUi:
    deck: DeckUi

    view: ContainerWidget

    def __init__(self, game: Game):
        self.view = ContainerWidget(
            QHBoxLayout(),
            align=Qt.AlignmentFlag.AlignCenter)

        self.deck = DeckUi(game.deck)
        self.view.style(
            {
                # "font-family": "Permanent Marker",
                "font-size": "20px",
            })
        self.view.add_widgets(NurseryArea(game.nursery), self.deck.view, DiscardArea(game.discard_pile))

    def update_after_draw(self):
        self.deck.update()
