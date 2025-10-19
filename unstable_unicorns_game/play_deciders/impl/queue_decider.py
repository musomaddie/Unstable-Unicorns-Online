""" A play decider which functions as a queue -> first in first out data structure. """
from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.play_deciders.discard_decider import DiscardDecider


class QueueDiscardDecider(DiscardDecider):
    def decide(self) -> Card:
        return self._hand.cards[0]
