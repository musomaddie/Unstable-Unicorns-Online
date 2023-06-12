from game_details.card import Card
from game_details.card.card_pile_manager import CardPileManager


class DeckManager(CardPileManager):
    """ Manages interactions with the current deck. """

    def __init__(self, cards=list[Card]):
        super().__init__(cards)
