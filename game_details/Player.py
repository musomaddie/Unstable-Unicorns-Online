import os
import sys

sys.path.insert(0, 
        os.path.dirname(os.path.realpath(__file__))[
            0:-len("game_details")])


from game_details.HandManager import HandManager
from game_details.StableManager import StableManager


class Player:
    """ Represents a player in the game.

    Parameters:
        name (str): the players name
        hand (HandManager): controls the state of the players hand.
        stable (StableManager): controls the players stable.
    """

    def __init__(self, name):
        self.name = name
        self.hand = HandManager(player=self)
        self.stable = StableManager(player=self)

    def __repr__(self):
        return f"{self.name} (player)"
