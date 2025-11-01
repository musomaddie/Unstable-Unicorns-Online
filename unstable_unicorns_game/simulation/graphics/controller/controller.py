from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget, Widget

start_button_styling = {
    "font-size": "20px"
    # TODO - additional styling!
}


class StartGameButton(Widget):

    def __init__(self):
        super().__init__(QPushButton("Start Game"))

        self.style(start_button_styling)


class Controller(ContainerWidget):
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top

        self.start_game_button = StartGameButton()

        self.add_widgets(self.start_game_button)
