from game_details.card import Card


class CardPileManager:
    """ A super class for managing anything that is a pile of cards (e.g. deck, discard pile). """

    def __init__(self, cards=list[Card]):
        self.cards = cards
