""" list of all players. """
from enum import Enum, auto

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.simulation.graphics.player import PlayerBoard
from unstable_unicorns_game.simulation.graphics.widget import Widget

color_list = [
    "#DEDAF4",
    "#D9EDF8",
    "#E4F1EE",
    "#FDFFB6",
    "#FFD6A5",
    "#FFADAD",
]


class ViewMode(Enum):
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()


class PlayersList(Widget):

    def __init__(self, players: AllPlayers):
        super().__init__(QVBoxLayout())

        self.view_mode = ViewMode.OVERVIEW
        self.player_boards = [PlayerBoard(player, color_code) for player, color_code in zip(players, color_list)]

        self.add_widgets(*[board.widget for board in self.player_boards])

    def update_view_mode(self, view_mode: ViewMode):
        print("I clicked it!")
        # Exit early if we're already in the desired mode.
        if view_mode == self.view_mode:
            return

        # TODO -> will need to determine in current player mode, how to represent where the current player is in
        #  terms of board area ??

        for player_board in self.player_boards:
            player_board.update_view_mode(view_mode)
