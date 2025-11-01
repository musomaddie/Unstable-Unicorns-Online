""" table top (center layout)"""
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.controller.controller import Controller
from unstable_unicorns_game.simulation.graphics.players_list import PlayersList
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenter
from unstable_unicorns_game.simulation.graphics.widget import Widget


class TableTop(Widget):

    def __init__(self, game: Game):
        super().__init__(QHBoxLayout())

        table_widget = Widget(QVBoxLayout())
        table_widget.add_widgets(TableCenter(game).widget, PlayersList(game.players).widget)
        self.add_widgets(
            Controller().widget,
            table_widget.widget)
