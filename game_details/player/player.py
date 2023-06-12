from dataclasses import dataclass

from game_details.hand import HandManager
from game_details.stable import StableManager


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand_manager: HandManager
    stable_manager: StableManager
