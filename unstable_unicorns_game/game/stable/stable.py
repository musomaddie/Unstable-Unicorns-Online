""" stable class """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.card.card import Card
from unstable_unicorns_game.game.card.card_type import CardType
from unstable_unicorns_game.game.card.multiple_cards_holder import MultipleCardsHolder


@dataclass
class Stable:
    """ Represents a stable."""
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder
    downgrades: MultipleCardsHolder

    @classmethod
    def create(cls, baby_unicorn: Card) -> Stable:
        """ Creates a stable containing only the given baby unicorn. """
        return cls(
            unicorns=MultipleCardsHolder.create_with_one_card(baby_unicorn),
            upgrades=MultipleCardsHolder.create_default(),
            downgrades=MultipleCardsHolder.create_default())

    @classmethod
    def create_default(cls) -> Stable:
        """ Creates a default stable. """
        return cls(
            unicorns=MultipleCardsHolder.create_with_one_card(
                Card.create_default("Baby Unicorn", CardType.BABY_UNICORN)),
            upgrades=MultipleCardsHolder.create_default(),
            downgrades=MultipleCardsHolder.create_default())
