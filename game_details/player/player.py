""" Player class """
from dataclasses import dataclass

from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.hand import Hand
from game_details.stable import Stable
from game_details.utilities import TurnActionType


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand
    stable: Stable

    @staticmethod
    def create_default(name: str) -> 'Player':
        """ Creates a player with the given name and otherwise default values. """
        return Player(name, Hand.create_default(), Stable.create_default())

    def take_beginning_of_turn_action(self) -> None:
        """ Handles the beginning of turn action. """
        pass

    def draw_card(self, deck: Deck) -> None:
        """ Removes the top card from the given deck and adds it to the hand. """
        self.hand.add_card(deck.draw_top())

    def discard_to_hand_limit(self, discard_pile: DiscardPile) -> None:
        """ Handles the process of discarding to the hand limit. """
        while self.hand.must_discard_to_limit():
            discard_pile.add_top(self.hand.choose_card_to_discard())

    @staticmethod
    def choose_play_card_or_draw() -> TurnActionType:
        """ Allows the players to choose if they would like to draw a card or play a card for their action."""

        # TODO - allow playing a card action.
        return TurnActionType.DRAW_CARD
