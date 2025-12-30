""" Manages interactions between the UI and the game. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.tabletop.table_top import TableTopUi, ViewMode
from unstable_unicorns_game.gui.widgets.button import Button
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


def toggle_button_container(toggle_button: Button) -> ContainerWidget:
    return ContainerWidget(
        QVBoxLayout(),
        children=[toggle_button],
        alignment=Qt.AlignmentFlag.AlignBottom,
        margins=Margins(bottom=20))


def game_control_buttons_container(start_btn: Button, draw_btn: Button) -> ContainerWidget:
    draw_btn.hide()
    return ContainerWidget(
        QVBoxLayout(),
        children=[start_btn, draw_btn],
        alignment=Qt.AlignmentFlag.AlignTop,
        margins=Margins(top=20))


class Controller:
    game: Game
    tabletop: TableTopUi
    view: ContainerWidget

    toggle_view_button: Button
    start_game_button: Button
    draw_action_button: Button

    def __init__(self, game: Game, tabletop: TableTopUi):
        self.game = game
        self.tabletop = tabletop
        self.toggle_view_button = Button("Compact view", self.toggle_players_view)
        self.start_game_button = Button("Start game", self.start_game)
        self.draw_action_button = Button("Draw a card", self.draw_action)

        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[
                game_control_buttons_container(self.start_game_button, self.draw_action_button),
                toggle_button_container(self.toggle_view_button), ],
            margins=Margins(right=20, left=20),
        )

    def set_toggle_button_text(self, view_mode: ViewMode):
        match view_mode:
            case ViewMode.CURRENT_PLAYER:
                self.toggle_view_button.update_text("Overview view")
            case ViewMode.OVERVIEW:
                self.toggle_view_button.update_text("Compact view")

    def start_game(self):
        # Make sure we're in current players view.
        self.tabletop.update_view(ViewMode.CURRENT_PLAYER)
        self.set_toggle_button_text(ViewMode.CURRENT_PLAYER)

        self.start_game_button.disable()
        self.start_game_button.hide()
        self.draw_action_button.show()
        self.tabletop.update_players_choice_text("Draw a card")

    def draw_action(self):
        self.game.take_draw_card_action()
        self.tabletop.update_ui(deck=True, hand=True)

        self.draw_action_button.disable()

    def toggle_players_view(self):
        new_view = ViewMode.CURRENT_PLAYER if self.tabletop.view_mode == ViewMode.OVERVIEW else ViewMode.OVERVIEW
        self.tabletop.update_view(new_view)
        self.set_toggle_button_text(new_view)
