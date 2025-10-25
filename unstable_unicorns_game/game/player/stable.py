""" stable class """
from __future__ import annotations

from dataclasses import dataclass

import unstable_unicorns_game.utilities.logger_keys as LK
from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.utilities.logger import Logger


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

    def log(self):
        """ Logs the current state of this stable. """
        log = Logger({LK.UNICORNS: self.unicorns.log_all()})
        log.unless_empty(LK.UPGRADES, self.upgrades)
        log.unless_empty(LK.DOWNGRADES, self.downgrades)
        return log
