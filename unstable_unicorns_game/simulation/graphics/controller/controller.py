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


class ToggleViewModelButton(Widget):
    table_top: TableTop
    view_mode: ViewMode
    button_text: str

    def __init__(self, table_top: TableTop):
        self.view_mode = ViewMode.EXPANDED
        self.table_top = table_top

        self.button = QPushButton(self._make_text())
        super().__init__(self.button)

        self.button.pressed.connect(lambda: self.toggle())
        self.style(start_button_styling)

    def toggle(self):
        if self.view_mode == ViewMode.EXPANDED:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
            self.button.setText(self._make_text())
        else:
            self.view_mode = ViewMode.EXPANDED
            self.table_top.make_expanded()
            self.button.setText(self._make_text())

    def _make_text(self):
        if self.view_mode == ViewMode.EXPANDED:
            return "View compact"
        return "View expanded"


class Controller(ContainerWidget):
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top

        self.start_game_button = StartGameButton(table_top)
        self.toggle_view_button = ToggleViewModelButton(table_top)
        self.widget.setFixedWidth(200)

        self.add_widgets(self.start_game_button, self.toggle_view_button)
