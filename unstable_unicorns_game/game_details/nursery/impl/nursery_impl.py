""" nursery impl. """
from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.nursery import Nursery


class NurseryImpl(Nursery):
    """ Implementation of nursery. """

    def get_baby(self) -> Card:
        return self.pop_top()
