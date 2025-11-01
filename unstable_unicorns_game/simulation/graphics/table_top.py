""" table top (center layout)"""
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.players_list import PlayersList
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenter
from unstable_unicorns_game.simulation.graphics.widget import Widget


class TableTop(Widget):

    def __init__(self, game: Game):
        super().__init__(QVBoxLayout())

        self.center = TableCenter(game)
        self.players = PlayersList(game.players)

        self.add_widgets(self.center.widget, self.players.widget)
