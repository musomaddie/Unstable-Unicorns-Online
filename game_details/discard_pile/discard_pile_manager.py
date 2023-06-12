from game_details.card.card import Card
from game_details.card.card_pile_manager import CardPileManager


class DiscardPile(CardPileManager):
    """ A manager for the discard pile."""

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
