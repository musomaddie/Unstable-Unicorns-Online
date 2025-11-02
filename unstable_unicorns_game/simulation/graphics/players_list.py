""" list of all players. """
from enum import Enum, auto

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.simulation.graphics.player import PlayerBoard
from unstable_unicorns_game.simulation.graphics.player.player_board import PlayerViewMode
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget

color_list = [
    "#DEDAF4",
    "#D9EDF8",
    "#E4F1EE",
    "#FDFFB6",
    "#FFD6A5",
    "#FFADAD",
]


class TableViewMode(Enum):
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()


class PlayersList(ContainerWidget):
    view_mode: TableViewMode
    player_boards: list[PlayerBoard]

    list_view: ContainerWidget
    summary_view: ContainerWidget

    def __init__(self, players: AllPlayers):
        super().__init__(QVBoxLayout())

        self.view_mode = TableViewMode.OVERVIEW
        self.player_boards = [PlayerBoard(player, color_code) for player, color_code in zip(players, color_list)]

        self.summary_view = ContainerWidget(QHBoxLayout())
        self.list_view = ContainerWidget(QVBoxLayout())

        self.list_view.add_widgets(*self.player_boards)

        self.add_widgets(self.list_view)

    def _apply_current_player_styling(self):
        # TODO -> handle current player!
        for board in self.player_boards:
            board.update_view_mode(PlayerViewMode.SUMMARISED)

        self.summary_view.add_widgets(*self.player_boards)
        self.add_widgets(self.summary_view)
        self.list_view.clear_layout()

    def update_view_mode(self, view_mode: TableViewMode):
        # Exit early if we're already in the desired mode.
        if view_mode == self.view_mode:
            return

        self.view_mode = view_mode
        if view_mode == TableViewMode.CURRENT_PLAYER:
            self._apply_current_player_styling()
        # TODO -> implement for overview.
