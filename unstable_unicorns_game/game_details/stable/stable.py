""" stable class """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.multiple_cards_holder import MultipleCardsHolder


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder
    downgrades: MultipleCardsHolder
