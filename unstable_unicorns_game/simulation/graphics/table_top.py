""" table top (center layout)"""
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.players_list import PlayersList
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenter
from unstable_unicorns_game.simulation.graphics.utility import Widget


class TableTop(Widget):

    def __init__(self, game: Game):
        super().__init__(QVBoxLayout())

        self.add_widgets(TableCenter(game).widget, PlayersList(game.players).widget)

        # table_widget = NestedWidget(QVBoxLayout())
        # table_
        # table_widget.add_widgets()
        # table_widget = QWidget()
        # table_widget.setLayout(QVBoxLayout())
        # table_widget.layout().addWidget(TableCenter.(game))
        # table_widget.layout().addWidget(PlayersList.(game.players))

        # self.add_widgets(
        #     table_widget)
