""" stable class """
from dataclasses import dataclass

from game_details.card import MultipleCardsHolder, Card, CardType


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder
    downgrades: MultipleCardsHolder

    @staticmethod
    def create_default() -> 'Stable':
        """ Create a default stable. """
        return Stable(
            unicorns=MultipleCardsHolder.create(Card.create_default("Baby Unicorn", CardType.BABY_UNICORN)),
            upgrades=MultipleCardsHolder.create_default(),
            downgrades=MultipleCardsHolder.create_default())

    @staticmethod
    def create(baby_unicorn):
        """ Creates a stable containing only the given baby unicorn. """
        return Stable(
            unicorns=MultipleCardsHolder.create(baby_unicorn),
            upgrades=MultipleCardsHolder.create_default(),
            downgrades=MultipleCardsHolder.create_default())
