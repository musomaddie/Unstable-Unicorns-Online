from game_details.card import CardPile
from game_details.card.card import Card


class Deck(CardPile):
    """ Manages interactions with the current deck. """

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
