""" container for all parent decider classes. """
from abc import abstractmethod, ABCMeta
from dataclasses import dataclass

from game_details.card import Card
from game_details.hand import Hand


@dataclass
class DiscardDecider(metaclass=ABCMeta):
    """ handles the discard stuff. """

    hand: Hand

    @abstractmethod
    def decide_discard(self) -> Card:
        """ Returns the card which should be discarded. """
        pass
