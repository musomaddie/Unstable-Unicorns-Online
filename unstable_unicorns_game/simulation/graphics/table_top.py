""" table top (center layout)"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from unstable_unicorns_game.game_details.game import Game
from unstable_unicorns_game.simulation.graphics.players_list import PlayersList
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenter
from unstable_unicorns_game.simulation.graphics.utility import Widget


class TableTop(Widget):
    @classmethod
    def create_widget(cls, game: Game) -> QWidget:
        return cls(game).widget

    def __init__(self, game: Game):
        super().__init__(QVBoxLayout())
        self.add_widgets(TableCenter.create_widget(), PlayersList.create_widget(game.players))
