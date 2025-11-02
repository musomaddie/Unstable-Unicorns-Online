from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.players_list import TableViewMode
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget, Widget

start_button_styling = {
    "font-size": "20px"
    # TODO - additional styling!
}


class StartGameButton(Widget):
    table_top: TableTop

    def __init__(self, table_top):
        button = QPushButton("Start Game")
        super().__init__(button)
        self.table_top = table_top

        button.pressed.connect(lambda: self.on_click())

        self.style(start_button_styling)

    def on_click(self):
        self.table_top.players.update_view_mode(TableViewMode.CURRENT_PLAYER)


class Controller(ContainerWidget):
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top

        self.start_game_button = StartGameButton(table_top)
        self.widget.setMaximumWidth(200)

        self.add_widgets(self.start_game_button)
