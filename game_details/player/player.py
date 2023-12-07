""" Player class """
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.hand import Hand
from game_details.stable import Stable
from game_details.utilities import TurnActionType


@dataclass
class Player(metaclass=ABCMeta):
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand
    stable: Stable

    @abstractmethod
    def take_beginning_of_turn_action(self) -> None:
        """ Handles the beginning of turn action. """
        pass

    @abstractmethod
    def draw_card(self, deck: Deck) -> None:
        """ Removes the top card from the given deck and adds it to the hand. """
        pass

    @abstractmethod
    def discard_to_hand_limit(self, discard_pile: DiscardPile) -> None:
        """ Handles the process of discarding to the hand limit. """
        pass

    @staticmethod
    @abstractmethod
    def choose_play_card_or_draw() -> TurnActionType:
        """ Allows the players to choose if they would like to draw a card or play a card for their action."""
        pass
