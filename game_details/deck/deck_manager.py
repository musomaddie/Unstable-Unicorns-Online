from game_details.card.card import Card
from game_details.card.card_pile_manager import CardPileManager


class Deck(CardPileManager):
    """ Manages interactions with the current deck. """

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
