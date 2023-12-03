""" deck implementation. """
from game_details.card import Card
from game_details.deck import Deck


class DeckImpl(Deck):
    """ Implementation of the deck. """

    def draw_top(self) -> Card:
        return self.pop_top()
