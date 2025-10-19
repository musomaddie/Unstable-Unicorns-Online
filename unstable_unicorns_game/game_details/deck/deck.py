""" Deck class """
from abc import ABCMeta
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_stack import CardStack


@dataclass
class Deck(CardStack, metaclass=ABCMeta):
    """ Manages interactions with the current deck. """

    def draw_top(self) -> Card:
        """ Removes and returns the top (first) card from this pile."""
        pass
