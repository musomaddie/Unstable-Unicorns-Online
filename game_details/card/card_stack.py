from dataclasses import dataclass

from game_details.card.multiple_cards_holder import MultipleCardsHolder


@dataclass
class CardStack(MultipleCardsHolder):

    def draw_top(self):
        """ Removes and returns the top (first) card from this pile."""
        return self.cards.pop(0)
