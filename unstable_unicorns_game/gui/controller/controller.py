""" Manages interactions between the UI and the game. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
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


def game_control_buttons_container(
        start_btn: Button,
        draw_btn: Button,
        play_card_btn: Button,
        draw_turn_btn: Button,
        end_turn_btn: Button) -> ContainerWidget:
    draw_btn.hide()
    play_card_btn.hide()
    play_card_btn.disable()
    draw_turn_btn.hide()
    draw_turn_btn.disable()
    end_turn_btn.hide()
    end_turn_btn.disable()

    return ContainerWidget(
        QVBoxLayout(),
        children=[start_btn, draw_btn, play_card_btn, draw_turn_btn, end_turn_btn],
        alignment=Qt.AlignmentFlag.AlignTop,
        margins=Margins(top=20))


class Controller:
    game: Game
    tabletop: TableTopUi
    view: ContainerWidget

    toggle_view_button: Button
    start_game_button: Button
    play_card_action_button: Button
    draw_action_button: Button
    draw_turn_action_button: Button
    end_turn_action_button: Button

    def __init__(self, game: Game, tabletop: TableTopUi):
        self.game = game
        self.tabletop = tabletop
        self.toggle_view_button = Button("Compact view", self.toggle_players_view)
        self.start_game_button = Button("Start game", self.start_game)
        self.draw_action_button = Button("Draw a card", self.draw_action)
        self.play_card_action_button = Button("Play a card", self.play_card_action)
        self.draw_turn_action_button = Button("Draw a card", self.draw_turn_action)
        self.end_turn_action_button = Button("End turn", self.end_turn)

        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[
                game_control_buttons_container(
                    self.start_game_button,
                    self.draw_action_button,
                    self.play_card_action_button,
                    self.draw_turn_action_button,
                    self.end_turn_action_button),
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
        self.play_card_action_button.show()
        self.draw_turn_action_button.show()
        self.end_turn_action_button.show()
        self.tabletop.update_players_choice_text("Draw a card")

    def draw_action(self):
        self.game.take_draw_card_action()

        self.tabletop.update_ui(deck=True, hand=True)

        self.draw_action_button.disable()
        self.draw_turn_action_button.enable()
        self.play_card_action_button.enable()

        self.tabletop.update_players_choice_text("Either draw or play")

    def draw_turn_action(self):
        # Differs from the method above as this is done when the player chooses to draw a card as their main turn
        # action.
        self.game.take_draw_card_action()
        self.tabletop.update_ui(deck=True, hand=True)

        # TODO -> defs create a game state manager thing and move button enability into there to make this cleaner /
        #  better.
        self.end_turn_action_button.enable()
        self.draw_turn_action_button.disable()
        self.play_card_action_button.disable()

    def play_card_action(self):
        self.tabletop.update_players_choice_text("Choose a card to play")
        self.tabletop.enable_card_choice(self.play_card_onclick)
        self.draw_turn_action_button.disable()
        self.play_card_action_button.disable()

    def play_card_onclick(self, card: Card):
        self.tabletop.update_players_choice_text("end turn ... ")
        self.tabletop.disable_card_choice()

        self.game.play_card_action(card)
        self.tabletop.update_ui(hand=True, stable=True)

        self.end_turn_action_button.enable()

    def end_turn(self):
        # Check the hand limit.
        if self.game.over_hand_limit():
            self.tabletop.update_players_choice_text("Must discard to hand limit. Choose a card to discard.")
            self.tabletop.enable_card_choice(self.discard_onclick)
            return

        # Otherwise, move to the next player
        self.game.next_player()
        print("turn end")
        self.end_turn_action_button.disable()
        self.tabletop.change_current_player(self.game.players.current_player())

    def toggle_players_view(self):
        new_view = ViewMode.CURRENT_PLAYER if self.tabletop.view_mode == ViewMode.OVERVIEW else ViewMode.OVERVIEW
        self.tabletop.update_view(new_view)
        self.set_toggle_button_text(new_view)

    def discard_onclick(self, card: Card):
        self.tabletop.update_players_choice_text("")
        self.tabletop.disable_card_choice()
        self.game.discard(card)
        self.tabletop.update_ui(hand=True, discard_pile=True)

        # This assumes that discard onclick was called from end_turn. Need to find a way to handle determining if it
        # was / wasn't. One option is to add a game state manager which handles the current state of the game. Use
        # that to determine next actions. Means we can also combine the draw onclick methods.
        self.end_turn()
