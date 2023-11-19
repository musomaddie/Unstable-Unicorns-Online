""" A play decider which functions as a queue -> first in first out data structure. """
from game_details.card import Card
from play_deciders.play_decider import PlayDecider


class QueueDecider(PlayDecider):
    def decide_discard(self) -> Card:
        return self.player.hand.cards[0]
