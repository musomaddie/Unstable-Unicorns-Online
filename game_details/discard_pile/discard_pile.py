from game_details.card import CardStack
from game_details.card.card import Card


class DiscardPile(CardStack):
    """ A manager for the discard pile."""

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
