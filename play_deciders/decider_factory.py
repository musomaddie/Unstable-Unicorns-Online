""" factory for creating the play decider. """
from enum import auto, Enum

from play_deciders.cli_decider import CliDecider
from play_deciders.queue_decider import QueueDecider


class DeciderType(Enum):
    """ enum to connect which decider will be used. """
    CLI = auto()
    QUEUE = auto()


class DeciderFactory:
    """ decider factory. """

    def __init__(self, decider_type: DeciderType):
        self.decider_type = decider_type

    def create(self, player: 'Player'):
        """ creates a decider for the given player. """
        if self.decider_type == DeciderType.CLI:
            return CliDecider(player)
        else:
            return QueueDecider(player)
