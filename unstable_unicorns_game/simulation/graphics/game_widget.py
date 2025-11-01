from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.controller.controller import Controller
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widget import Widget


class GameWidget(Widget):

    def __init__(self, game: Game):
        super().__init__(QHBoxLayout())

        self.table_top = TableTop(game)
        self.controller = Controller(game, self.table_top)

        self.add_widgets(self.controller.widget, self.table_top.widget)
