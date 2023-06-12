from dataclasses import dataclass

from game_details.card import Card


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns = list[Card]
    upgrades = list[Card]
    downgrades = list[Card]
