# This class is a bit of a pain, because we construct it before we know what the hand variable is.
from abc import ABC, abstractmethod

from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.hand import Hand


class DiscardDecider(ABC):

    def __init__(self, hand: Hand):
        # Default by setting the hand to none.
        self._hand = hand

    def _determine_valid_discard_numbers(self):
        return [str(i + 1) for i in range(len(self._hand))]

    def _get_chosen_card(self, num: str):
        return self._hand[int(num) - 1]

    @abstractmethod
    def decide(self) -> Card | None:
        """ Returns the card which should be discarded, or none if there are no cards to discard. Throws an error if
        the decider is in an illegal state. """
        pass
