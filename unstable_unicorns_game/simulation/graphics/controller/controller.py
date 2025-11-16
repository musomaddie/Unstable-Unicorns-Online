from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget

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


def _create_draw_card_button(onClick) -> Button:
    button = Button("Draw card", lambda: onClick())
    button.hide()
    return button


class Controller(ContainerWidget):
    game: Game
    game_started: bool = False

    table_top: TableTop
    view_mode: ViewMode

    start_game_button: Button
    toggle_view_button: Button
    draw_card_button: Button

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top
        self.view_mode = ViewMode.EXPANDED

        self.start_game_button = Button("Start Game", self.start_game)
        self.draw_card_button = _create_draw_card_button(self.draw_card)
        self.toggle_view_button = Button(self.view_mode.make_button_text(), self.toggle_view_mode)

        bottom_widget = ContainerWidget(QVBoxLayout())
        bottom_widget.set_margins(bottom=50)
        bottom_widget.add_widgets(self.toggle_view_button)
        bottom_widget.align(Qt.AlignmentFlag.AlignBottom)

        self.add_widgets(self.start_game_button, self.draw_card_button, bottom_widget)

        self.widget.setFixedWidth(250)

    def start_game(self):
        if self.view_mode == ViewMode.EXPANDED:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
            self.toggle_view_button.update_text(self.view_mode.make_button_text())

        if self.game_started:
            return
        self.start_game_button.button.setEnabled(False)
        self.draw_card_button.show()
        self.game_started = True

    def toggle_view_mode(self):
        if self.view_mode == ViewMode.EXPANDED:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
        else:
            self.view_mode = ViewMode.EXPANDED
            self.table_top.make_expanded()

        self.toggle_view_button.update_text(self.view_mode.make_button_text())

    def draw_card(self):
        self.table_top.draw_card()
        self.draw_card_button.button.setEnabled(False)
