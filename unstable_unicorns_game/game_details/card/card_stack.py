""" Card stack but it's really just a list. """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.card.multiple_cards_holder import MultipleCardsHolder


@dataclass
class CardStack(MultipleCardsHolder):

    @staticmethod
    def create_default() -> 'CardStack':
        """ Returns card stack made from an empty list. """
        return CardStack([])

    def add_top(self, card: Card) -> None:
        """ Adds the given card to the top of this stack."""
        self.cards.insert(0, card)

    def pop_top(self) -> Card:
        """ Removes and returns the first card in this stack. """
        return self.cards.pop(0)
