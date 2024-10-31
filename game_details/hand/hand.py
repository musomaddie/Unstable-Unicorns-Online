""" Hand class """
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from game_details.card import Card, MultipleCardsHolder


@dataclass
class Hand(MultipleCardsHolder, metaclass=ABCMeta):

    limit: int = 7

    @abstractmethod
    def add_card(self, card: Card) -> None:
        """ Adds the given card to this hand. """
        pass

    @abstractmethod
    def must_discard_to_limit(self) -> bool:
        """ Returns whether the hand has more cards than the limit """
        pass

    @abstractmethod
    def choose_card_to_discard(self) -> Card | None:
        """ Handles the process of choosing a card to discard from this hand. Will continue until a valid card to
        remove has been chosen, and returns it. """
        pass

    @abstractmethod
    def print_basics_with_index(self) -> None:
        """ Print the basic card info with an index. """
        pass
