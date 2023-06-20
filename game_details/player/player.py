from dataclasses import dataclass, field

from game_details.card import CardStack
from game_details.hand import Hand
from game_details.stable import Stable


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
