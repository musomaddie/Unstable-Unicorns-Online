from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.table_center.table_center import TableCenterUi
from unstable_unicorns_game.gui.tabletop.players_space import PlayersSpaceUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class TableTopUi:
    """
    Contains the entire game board (but not the controller). This includes the deck, discard pile, nursery, and players.
    """
    table_center: TableCenterUi
    players_space: PlayersSpaceUi
    view: ContainerWidget

    def __init__(self, game: Game):
        self.table_center = TableCenterUi(game)
        self.players_space = PlayersSpaceUi(game.players)
        self.view = ContainerWidget(
            QVBoxLayout(), children=[
                self.table_center.view,
                self.players_space,
            ])
