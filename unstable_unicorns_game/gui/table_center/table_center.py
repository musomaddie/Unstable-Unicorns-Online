from PyQt6.QtWidgets import QHBoxLayout, QLabel

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.table_center.deck_ui import DeckUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class TableCenterUi:
    view: ContainerWidget
    deck: DeckUi

    def __init__(self, game: Game):
        self.deck = DeckUi(game.deck)
        self.view = ContainerWidget(
            QHBoxLayout(),
            children=[
                Widget(widget=QLabel("Table Center")),
                self.deck.view
            ]
        )
