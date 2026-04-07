""" Think of this as a delegator between user actions and game state -> whenever the user does something,
this should be able to figure out how to handle it and what to do next. """
from enum import Enum, auto
from typing import Optional

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.game.player.player import Player


class TurnPhase(Enum):
    BEGINNING = auto()
    # TODO -> not sure how to use "beginning" well at this point, but we'll get there.
    DRAWING = auto()
    PLAYING = auto()
    PLAYING_PLAY = auto()
    PLAYING_DRAW = auto()
    ENDING = auto()


class GameState(Enum):
    SETUP = auto()
    PLAYING = auto()
    ENDING = auto()


class PendingUserChoice(Enum):
    NONE = auto()
    CARD_FROM_HAND = auto()
    ACTION = auto()


class GameLifecycleException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


# TODO -> this will need to handle cases where a player other than the current player is doing stuff.

class GameStateManager:

    game: Game
    turn_phase: TurnPhase
    game_state: GameState
    pending_choice: PendingUserChoice
    # TODO -> allow winning
    winner: Optional[Player] = None

    def __init__(self, game: Game):
        self.game = game
        self.game_state = GameState.SETUP
        self.turn_phase = TurnPhase.BEGINNING
        self.pending_choice = PendingUserChoice.NONE

    def start_game(self):
        if self.game_state != GameState.SETUP:
            raise GameLifecycleException("Cannot restart an already started game.")
        self.game_state = GameState.PLAYING
        self.turn_phase = TurnPhase.DRAWING
        self.pending_choice = PendingUserChoice.NONE
        self.draw_card()

    def draw_card(self):
        """ Draw a card and move to the next game state. """
        # Only draw a card if that's a valid choice.
        if self.turn_phase != TurnPhase.DRAWING or self.turn_phase != TurnPhase.PLAYING_DRAW:
            raise GameLifecycleException(f"Cannot draw a card while in {self.turn_phase.name} phase.")

        self.game.take_draw_card_action()

        if self.turn_phase == TurnPhase.PLAYING_DRAW:
            self.turn_phase = TurnPhase.ENDING
        elif self.turn_phase == TurnPhase.DRAWING:
            self.turn_phase = TurnPhase.PLAYING
            self.pending_choice = PendingUserChoice.ACTION

    def choose_draw_or_play(self, will_play: bool):
        if self.turn_phase != TurnPhase.PLAYING:
            raise GameLifecycleException(f"Cannot choose to draw or play while in {self.turn_phase.name} phase.")

        if will_play:
            self.turn_phase = TurnPhase.PLAYING_PLAY
            self.pending_choice = PendingUserChoice.CARD_FROM_HAND
            return

        self.turn_phase = TurnPhase.PLAYING_DRAW
        self.pending_choice = PendingUserChoice.NONE
        self.draw_card()

    def play_card(self, card: Card):
        # TODO -> allow playing at other times ??
        if self.turn_phase != TurnPhase.PLAYING_PLAY:
            raise GameLifecycleException(f"Cannot play a card while in {self.turn_phase.name} phase.")

        self.game.play_card_action(card)

        self.turn_phase = TurnPhase.ENDING
        self.pending_choice = PendingUserChoice.NONE
        self.end_turn()

    def discard(self, card: Card):
        if self.turn_phase != TurnPhase.ENDING:
            raise GameLifecycleException(f"Cannot discard a card while in {self.turn_phase.name} phase.")
        # TODO -> handle discarding a card outside of the ending phase as well as on other players turns.
        self.game.discard(card)

        self.pending_choice = PendingUserChoice.NONE
        self.end_turn()

    def end_turn(self):
        if self.game.over_hand_limit():
            self.pending_choice = PendingUserChoice.CARD_FROM_HAND
            return

        self.game.next_player()

        self.turn_phase = TurnPhase.DRAWING
        self.pending_choice = PendingUserChoice.NONE

        self.draw_card()
