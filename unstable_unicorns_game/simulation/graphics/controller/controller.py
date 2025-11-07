from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
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
        self.table_top.make_compact()


class ExpandViewButton(Widget):
    table_top: TableTop

    def __init__(self, table_top):
        button = QPushButton("Expand View")
        super().__init__(button)
        self.table_top = table_top

        button.pressed.connect(lambda: self.on_click())

        self.style(start_button_styling)

    def on_click(self):
        self.table_top.make_expanded()


class Controller(ContainerWidget):
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top

        self.start_game_button = StartGameButton(table_top)
        self.expand_button = ExpandViewButton(table_top)
        self.widget.setMaximumWidth(200)

        self.add_widgets(self.start_game_button, self.expand_button)
