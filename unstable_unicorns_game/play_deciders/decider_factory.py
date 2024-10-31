""" factory for creating the play decider. """
from enum import auto, Enum

from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.play_deciders.cli_decider import CliDiscardDecider
from unstable_unicorns_game.play_deciders.play_decider import DiscardDecider
from unstable_unicorns_game.play_deciders.queue_decider import QueueDiscardDecider


class DeciderType(Enum):
    """ enum to connect which decider will be used. """
    CLI = auto()
    QUEUE = auto()


class DeciderFactory:
    """ decider factory. """

    def __init__(self, decider_type: DeciderType):
        self.decider_type = decider_type

    def create_discard(self, hand: Hand) -> DiscardDecider:
        """ Creates a discard decider for the given hand. """
        if self.decider_type == DeciderType.CLI:
            return CliDiscardDecider(hand)
        else:
            return QueueDiscardDecider(hand)
