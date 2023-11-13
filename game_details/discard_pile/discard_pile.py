""" Discard Pile """
from dataclasses import dataclass

from game_details.card import CardStack


@dataclass
class DiscardPile(CardStack):
    """ A manager for the discard pile."""

    @staticmethod
    def create_default() -> 'DiscardPile':
        """ Creates an empty discard pile. """
        return DiscardPile(cards=[])
