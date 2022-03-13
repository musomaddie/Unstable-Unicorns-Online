import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])
from game_details.CardPileManager import CardPileManager

class DeckManager(CardPileManager):
    """ Managers the deck. Responsible for all interaction. 

    Parameters:
        cards (list<Card>): the cards currently in the deck
    """

    def __init__(self, cards):
        super().__init__(cards)

    def __repr__(self):
        return f"The deck with {len(self.cards)} cards"
