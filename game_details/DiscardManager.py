import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])
from game_details.CardPileManager import CardPileManager

class DiscardManager(CardPileManager):
    """ Manages the discard pile. Responsible for all interactions.

    Parameters:
        cards: the cards currently in the discard pile.
    """

    def __init__(self, cards):
        super().__init__(cards)

    def __repr__(self):
        return f"Discard pile with {len(self.cards)} cards"
