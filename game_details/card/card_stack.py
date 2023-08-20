from dataclasses import dataclass

from game_details.card import Card
from game_details.card.multiple_cards_holder import MultipleCardsHolder


@dataclass
class CardStack(MultipleCardsHolder):

    def add_top(self, card: Card) -> None:
        """ Adds the given card to the top of this stack."""
        self.cards.insert(0, card)

    def pop_top(self):
        """ Removes and returns the first card in this stack. """
        return self.cards.pop(0)
