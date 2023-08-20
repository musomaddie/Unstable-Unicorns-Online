from dataclasses import dataclass, field

from game_details.card import MultipleCardsHolder


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder = field(default_factory=list)
    downgrades: MultipleCardsHolder = field(default_factory=list)

    @staticmethod
    def create_stable(baby_unicorn):
        return Stable(unicorns=MultipleCardsHolder([baby_unicorn]))
