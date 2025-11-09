from enum import Enum

from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget, Widget

start_button_styling = {
    "font-size": "20px"
    # TODO - additional styling!
}


class ViewMode(Enum):
    COMPACT = "compact"
    EXPANDED = "expanded"

    def make_button_text(self):
        if self == ViewMode.COMPACT:
            return "View expanded"
        return "View compact"


class Button(Widget):
    button: QPushButton

    def __init__(self, text: str, onClick):
        self.button = QPushButton(text)
        super().__init__(self.button)

        self.button.pressed.connect(lambda: onClick())
        self.style(start_button_styling)

    def update_text(self, text: str):
        self.button.setText(text)


class Controller(ContainerWidget):
    game: Game
    table_top: TableTop
    view_mode: ViewMode
    start_game_button: Button
    toggle_view_button: Button

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top
        self.view_mode = ViewMode.EXPANDED

        self.start_game_button = Button("Start Game", self.start_game)
        self.toggle_view_button = Button(self.view_mode.make_button_text(), self.toggle_view_mode)
        self.add_widgets(self.start_game_button, self.toggle_view_button)

        self.widget.setFixedWidth(200)

    def start_game(self):
        if not self.table_top.is_compact:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
            self.toggle_view_button.update_text(self.view_mode.make_button_text())
        # Starting the game (for now) is just putting this in compact mode, nothing else needs to be done.

    def toggle_view_mode(self):
        if self.view_mode == ViewMode.EXPANDED:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
        else:
            self.view_mode = ViewMode.EXPANDED
            self.table_top.make_expanded()

        self.toggle_view_button.update_text(self.view_mode.make_button_text())
        pass
