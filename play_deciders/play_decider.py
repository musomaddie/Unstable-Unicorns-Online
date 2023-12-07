""" parent class for all play deciders. """
from abc import abstractmethod, ABCMeta
from dataclasses import dataclass

from game_details.card import Card
from game_details.hand import Hand


# class PlayDecider:
#     """
#     Class definition for all play deciders.
#
#     """
#
#     def __init__(self, this_player: 'Player'):
#         self.player = this_player
#
#     @abstractmethod
#     def decide_discard(self) -> Card:
#         """ Returns the card which should be discarded. """
#         pass


# TODO -> subclass this nicely, and maybe delegate so reduce complexity.
@dataclass
class DiscardDecider(metaclass=ABCMeta):
    """ handles the discard stuff. """

    hand: Hand

    @abstractmethod
    def decide_discard(self) -> Card:
        """ Returns the card which should be discard. """
        pass
