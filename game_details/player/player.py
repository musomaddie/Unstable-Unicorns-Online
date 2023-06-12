from dataclasses import dataclass, field

from game_details.hand import Hand
from game_details.stable import Stable


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand = field(default_factory=Hand)
    stable: Stable = field(default_factory=Stable)
