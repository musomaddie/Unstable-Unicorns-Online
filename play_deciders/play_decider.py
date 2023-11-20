""" parent class for all play deciders. """
from abc import abstractmethod

from game_details.card import Card


class PlayDecider:
    """
    Class definition for all play deciders.

    """

    def __init__(self, this_player: 'Player'):
        self.player = this_player

    @abstractmethod
    def decide_discard(self) -> Card:
        """ Returns the card which should be discarded. """
        pass
