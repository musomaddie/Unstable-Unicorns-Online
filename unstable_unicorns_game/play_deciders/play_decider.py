""" container for all parent decider classes. """
from dataclasses import dataclass, field

from unstable_unicorns_game.play_deciders.cli_decider import CliDiscardDecider
from unstable_unicorns_game.play_deciders.decider_type import DeciderType
from unstable_unicorns_game.play_deciders.queue_decider import QueueDiscardDecider
from unstable_unicorns_game.play_deciders.test_decider import TestDiscardDecider


@dataclass
class PlayDecider:
    """ Describes and handles how decisions should be made throughout the game. """
    decider_type: DeciderType
    decisions: list[str] = field(default_factory=list)

    def create_discard_decider(self, hand):
        if self.decider_type == DeciderType.CLI:
            return CliDiscardDecider(hand)
        if self.decider_type == DeciderType.QUEUE:
            return QueueDiscardDecider(hand)
        return TestDiscardDecider(hand, self.decisions)
