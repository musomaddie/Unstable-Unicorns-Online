from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.table_center.table_center import TableCenterUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class TableTopUi:
    """
    Contains the entire game board (but not the controller). This includes the deck, discard pile, nursery, and players.
    """
    table_center: TableCenterUi
    view: ContainerWidget

    def __init__(self, game: Game):
        self.table_center = TableCenterUi(game)
        self.view = ContainerWidget(QVBoxLayout(), children=[self.table_center.view])
