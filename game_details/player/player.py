from dataclasses import dataclass, field

from game_details.card import CardStack
from game_details.hand import Hand
from game_details.stable import Stable
from game_details.utilities import ActionType


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand = field(default_factory=Hand)
    stable: Stable = field(default_factory=Stable)

    def take_beginning_of_turn_action(self) -> None:
        """ Handles the beginning of turn action. """
        pass

    def draw_card(self, deck: CardStack) -> None:
        """ Removes the top card from the given deck and adds it to the hand. """
        self.hand.add_card(deck.draw_top())
        
    def discard_to_hand_limit(self) -> None:
        pass

    @staticmethod
    def choose_play_card_or_draw() -> ActionType:
        """ Allows the players to choose if they would like to draw a card or play a card for their action."""

        # TODO - allow playing a card action.
        return ActionType.DRAW_CARD
