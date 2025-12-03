from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.utility.measurements import Margins
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


# TODO -> can I clean this up and make it easier to follow at all??

class GameControlButtons(ContainerWidget):
    start: Button
    draw: Button
    draw_choice: Button
    play_choice: Button
    end_turn: Button

    def __init__(self, on_start_click, on_draw_click, on_draw_choice_click, on_play_choice_click, on_end_turn_click, ):
        super().__init__(QVBoxLayout(), align=Qt.AlignmentFlag.AlignTop, margins=Margins(top=20), remove_margins=True)

        self.start = Button("Start Game", on_start_click)
        turn_label = CenteredLabel("Turn Actions")
        self.draw = Button("Draw card", on_draw_click)

        choice_label = CenteredLabel("Choose one of the following", word_wrap=True, style_identifier="small-lbl")
        self.draw_choice = Button("Draw a card", on_draw_choice_click)
        self.play_choice = Button("Play a card", on_play_choice_click)
        self.end_turn = Button("End turn", on_end_turn_click)

        self.turn_body = ContainerWidget(QVBoxLayout(), style_identifier="container", styling=styles.turn_buttons())
        self.turn_body.add_widgets(choice_label, self.draw_choice, self.play_choice)

        self.turn_widget = ContainerWidget(QVBoxLayout(), style_identifier="container", styling=styles.turn_buttons())
        self.turn_widget.add_widgets(turn_label, self.draw, self.turn_body)

        self.add_widgets(self.start, self.turn_widget)

        self.turn_body.hide()
        self.turn_widget.hide()
        self.disable_stretching()

    def start_game(self):
        self.start.disable()
        self.turn_widget.show()
        self.turn_body.hide()

    def card_drawn(self):
        self.draw.disable()
        self.turn_body.show()

    def after_choice(self):
        self.draw_choice.disable()
        self.play_choice.disable()


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

        self.game_buttons = GameControlButtons(
            self.start_game, self.draw_card, self.draw_card_choice, self.play_card, lambda: None)
        self.toggle_view_button = Button(self.view_mode.make_button_text(), self.toggle_view_mode)

        bottom_widget = ContainerWidget(QVBoxLayout(), align=Qt.AlignmentFlag.AlignBottom)
        bottom_widget.add_widgets(self.toggle_view_button)

        bottom_widget.set_margins(Margins(bottom=50))

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
        self.game.take_draw_card_action()
        self.table_top.update_ui_after_draw()
        self.game_buttons.card_drawn()

    def draw_card_choice(self):
        self.game.take_draw_card_action()
        self.table_top.update_ui_after_draw()
        self.game_buttons.after_choice()

    def play_card(self):
        self.table_top.prepare_choose_card_to_play(self.play_card_onclick)

    def play_card_onclick(self, card: Card):
        self.game.play_card_action(card)
        # Update the hand and stable to show the card has moved.

        self.game_buttons.after_choice()

    def other_play_card_behavior(self):
        self.table_top.cleanup_choose_card_to_play()
        self.game_buttons.after_choice()
