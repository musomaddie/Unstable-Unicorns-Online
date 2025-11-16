from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.utility import styles
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

    def __init__(self, text: str, on_click):
        self.button = QPushButton(text)
        super().__init__(self.button)

        self.button.pressed.connect(lambda: on_click())
        self.style(start_button_styling)

    def update_text(self, text: str):
        self.button.setText(text)


def _create_draw_card_button(on_click) -> Button:
    button = Button("Draw card", lambda: on_click())
    button.hide()
    return button


def create_divider() -> ContainerWidget:
    w = ContainerWidget(QVBoxLayout())
    w.style_with_selectors(styles.horizontal_line())
    w.minimum_size(height=4)
    return w


class TurnButtons(ContainerWidget):
    """ A holder for the buttons that controller turn actions. """
    draw_action: Button
    draw_choice: Button
    play_choice: Button

    def __init__(self, draw_action):
        super().__init__(QVBoxLayout())
        self.draw_action = _create_draw_card_button(draw_action)
        div = create_divider()
        self.draw_choice = Button("Draw a card", lambda: None)
        self.play_choice = Button("Play a card", lambda: None)
        div2 = create_divider()
        div.hide()
        div2.hide()
        self.draw_choice.hide()
        self.play_choice.hide()

        self.add_widgets(
            self.draw_action,
            div,
            self.draw_choice,
            self.play_choice,
            div2
        )

        self.disable_stretching()


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

        top_widget = ContainerWidget(QVBoxLayout())
        top_widget.set_margins(top=20)
        top_widget.align(Qt.AlignmentFlag.AlignTop)

        self.start_game_button = Button("Start Game", self.start_game)
        padding_label = create_divider()
        turn_buttons = TurnButtons(self.draw_card)
        self.draw_card_button = turn_buttons.draw_action
        self.toggle_view_button = Button(self.view_mode.make_button_text(), self.toggle_view_mode)

        bottom_widget = ContainerWidget(QVBoxLayout())
        bottom_widget.set_margins(bottom=50)
        bottom_widget.add_widgets(self.toggle_view_button)
        bottom_widget.align(Qt.AlignmentFlag.AlignBottom)
        top_widget.add_widgets(
            self.start_game_button, padding_label, turn_buttons)
        top_widget.disable_stretching()

        self.add_widgets(
            top_widget,
            bottom_widget)

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
