""" Deck class """
from abc import ABCMeta
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import CardStack, Card


@dataclass
class Deck(CardStack, metaclass=ABCMeta):
    """ Manages interactions with the current deck. """

    def draw_top(self) -> Card:
        """ Removes and returns the top (first) card from this pile."""
        pass
