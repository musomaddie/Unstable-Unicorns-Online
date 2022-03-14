import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])
from game_details.Card import Card

class NurseryManager:
    """ Manages all interactions with the nursery. The babies themselves will
    not be important until images are taken into account to make them unique.

    Parameters:
        cards (list<CardManager>): the list of cards in the nursery.

    Methods:
        remove_from_nursery: removes and returns a baby from the nursery.
    """

    def __init__(self):
        # Creating the nursery with 30 babies for now.
        # TODO: there are no babies in the database at the moment. This will
        # need to change when images are considered.
        baby_unicorn_fields = ["Baby Unicorn", 
                "Baby Unicorn", 
                "Baby Unicorn - Cute"]
        for _ in range(15):
            baby_unicorn_fields.append(False)
        baby_unicorn = Card(*baby_unicorn_fields)
        self.cards = []
        for _ in range(30):
            self.cards.append(copy.copy(baby_unicorn))


    def remove_from_nursery(self):
        """ Removes and returns the topmost baby. Will later be modified to
        return baby of choice.

        Returns:
            baby (Card): the baby that has been removed
        """
        return self.cards.pop(0)



