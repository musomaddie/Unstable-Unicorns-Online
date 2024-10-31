""" stable class """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import MultipleCardsHolder


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder
    downgrades: MultipleCardsHolder
