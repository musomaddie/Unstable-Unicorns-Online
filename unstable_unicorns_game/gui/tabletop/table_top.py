from enum import Enum, auto

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.table_center.table_center import TableCenterUi
from unstable_unicorns_game.gui.tabletop.players_space import PlayersSpaceUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class ViewMode(Enum):
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()


class TableTopUi:
    """
    Contains the entire game board (but not the controller). This includes the deck, discard pile, nursery, and players.
    """
    table_center: TableCenterUi

    players_space: PlayersSpaceUi
    view: ContainerWidget

    view_mode: ViewMode

    def __init__(self, game: Game):
        self.table_center = TableCenterUi(game)
        self.players_space = PlayersSpaceUi(game.players)
        self.view_mode = ViewMode.OVERVIEW
        self.view = ContainerWidget(
            QVBoxLayout(), children=[
                self.table_center.view,
                self.players_space,
            ])

    def update_view(self, view_mode: ViewMode):
        if view_mode == self.view_mode:
            return

        match view_mode:
            case ViewMode.OVERVIEW:
                self.players_space.use_overview_view()
            case ViewMode.CURRENT_PLAYER:
                self.players_space.use_players_view()

        self.view_mode = view_mode
