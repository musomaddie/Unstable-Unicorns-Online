""" Python module for play deciders -> i.e, what makes decisions regarding which cards to play. """

from .cli_decider import CliDiscardDecider
from .factory import DeciderFactory, DeciderType
from .queue_decider import QueueDiscardDecider
