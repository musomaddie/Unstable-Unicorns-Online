from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.button import Button
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


class ViewMode(Enum):
    COMPACT = "compact"
    EXPANDED = "expanded"

    def make_button_text(self):
        if self == ViewMode.COMPACT:
            return "View expanded"
        return "View compact"


class GameControlButtons(ContainerWidget):
    start: Button
    draw: Button
    draw_choice: Button
    play_choice: Button

    def __init__(self, on_start_click, on_draw_click):
        super().__init__(QVBoxLayout())
        self.set_margins(top=20)
        self.align(Qt.AlignmentFlag.AlignTop)

        self.start = Button("Start Game", on_start_click)
        turn_label = CenteredLabel("Turn Actions")
        self.draw = Button("Draw card", on_draw_click)

        self.turn_widget = ContainerWidget(QVBoxLayout(), style_identifier="container")
        self.turn_widget.style_with_selectors(styles.turn_buttons())
        self.turn_widget.add_widgets(turn_label, self.draw)

        self.add_widgets(self.start, self.turn_widget)

        self.turn_widget.hide()
        self.remove_margins()
        self.disable_stretching()

    def start_game(self):
        self.start.disable()
        self.turn_widget.show()


class Controller(ContainerWidget):
    game: Game
    game_started: bool = False

    table_top: TableTop
    view_mode: ViewMode

    game_buttons: GameControlButtons
    toggle_view_button: Button

    def __init__(self, game: Game, table_top: TableTop):
        super().__init__(QVBoxLayout())
        self.game = game
        self.table_top = table_top
        self.view_mode = ViewMode.EXPANDED

        self.game_buttons = GameControlButtons(self.start_game, self.draw_card)

        self.toggle_view_button = Button(self.view_mode.make_button_text(), self.toggle_view_mode)

        bottom_widget = ContainerWidget(QVBoxLayout())
        bottom_widget.set_margins(bottom=50)
        bottom_widget.add_widgets(self.toggle_view_button)
        bottom_widget.align(Qt.AlignmentFlag.AlignBottom)

        self.add_widgets(self.game_buttons, bottom_widget)

        self.widget.setFixedWidth(250)

    def start_game(self):
        if self.view_mode == ViewMode.EXPANDED:
            self.view_mode = ViewMode.COMPACT
            self.table_top.make_compact()
            self.toggle_view_button.update_text(self.view_mode.make_button_text())

        if self.game_started:
            return
        self.game_buttons.start_game()
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
        self.game_buttons.draw.disable()
