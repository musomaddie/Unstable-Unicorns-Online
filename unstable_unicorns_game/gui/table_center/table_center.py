from PyQt6.QtWidgets import QHBoxLayout, QLabel

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class TableCenterUi:
    view: ContainerWidget

    def __init__(self, game: Game):
        self.view = ContainerWidget(
            QHBoxLayout(),
            children=[
                Widget(widget=QLabel("Table Center")),
                Widget(widget=QLabel(f"Deck with {len(game.deck)} cards"))
            ]
        )
