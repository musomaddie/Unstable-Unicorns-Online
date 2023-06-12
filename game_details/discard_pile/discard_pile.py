from game_details.card import CardPile
from game_details.card.card import Card


class DiscardPile(CardPile):
    """ A manager for the discard pile."""

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
