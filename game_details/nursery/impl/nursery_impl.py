""" nursery impl. """
from game_details.card import Card
from game_details.nursery import Nursery


class NurseryImpl(Nursery):
    """ Implementation of nursery. """

    def get_baby(self) -> Card:
        return self.pop_top()
