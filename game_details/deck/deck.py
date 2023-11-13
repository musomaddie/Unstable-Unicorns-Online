""" Deck class """
from dataclasses import dataclass

from game_details.card import CardStack, Card


@dataclass
class Deck(CardStack):
    """ Manages interactions with the current deck. """

    @staticmethod
    def create_default() -> 'Deck':
        return Deck(cards=[])

    @staticmethod
    def create(card: Card) -> 'Deck':
        return Deck(cards=[card])

    def draw_top(self) -> Card:
        """ Removes and returns the top (first) card from this pile."""
        return self.pop_top()
