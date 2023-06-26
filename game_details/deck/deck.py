from dataclasses import dataclass

from game_details.card import CardStack


@dataclass
class Deck(CardStack):
    """ Manages interactions with the current deck. """

    def draw_top(self):
        """ Removes and returns the top (first) card from this pile."""
        return self.cards.pop(0)
