class CardPileManager:
    """ A super class for the cards that function as "piles" including the
    deck and the discard pile. 

    Parameters:
        cards (list<Card>): the cards that are currently in the pile.
    """

    def __init__(self, cards):
        self.cards = cards
