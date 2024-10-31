""" Nursery class file """
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import Card, CardStack


@dataclass
class Nursery(CardStack, metaclass=ABCMeta):
    """ Managers the nursery. """
    cards: list[Card]

    @abstractmethod
    def get_baby(self) -> Card:
        """ Removes and returns the first baby from the nursery. """
        pass
