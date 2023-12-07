""" A play decider which functions as a queue -> first in first out data structure. """
from game_details.card import Card
from play_deciders.play_decider import DiscardDecider


class QueueDiscardDecider(DiscardDecider):
    def decide_discard(self) -> Card:
        return self.hand.cards[0]
