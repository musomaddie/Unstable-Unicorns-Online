from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widget import Widget


class Controller(Widget):
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        button = QPushButton("Compact")

        self.add_widgets(button)
        # TODO -> consider if I want this to be a custom widget / button at all.
        # self.player_list = player_list
        self.game = game
        self.table_top = table_top

    # def on_compact_click(self):
    #     self.player_list.update_view_mode(TableViewMode.CURRENT_PLAYER)
