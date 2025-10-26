""" File for card stuff """
from __future__ import annotations

from dataclasses import dataclass

import unstable_unicorns_game.utilities.logger_keys as LK
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.effect.effect import Effect
from unstable_unicorns_game.utilities.logger import Logger


@dataclass
class Card:
    """ Class for holding information about a card within the deck. """

    name: str
    card_type: CardType
    text: str
    effect: Effect

    @classmethod
    def create_default(cls, name: str, card_type: CardType) -> Card:
        """Create a Card with the given name and type using default values for other fields."""
        return cls(name=name, card_type=card_type, text="default text", effect=Effect.create_default())

    @classmethod
    def create(cls, card_info: dict) -> "Card":
        """ Creates a card from the given dictionary. """
        return cls(
            card_info["name"],
            CardType.create(card_info["type"]),
            card_info["text"],
            Effect.create(card_info)
        )

    def log(self) -> Logger:
        """ Creates and returns a log for this card. """
        # TODO -> update what we store here -> probably minimal info to avoid bloat, since we can look up the
        #  unicorns in the original dict regardless.
        # TODO -> make an identifier for the cards (i.e. for those who just have a diff image vs name) and use that
        #  here instead.
        return Logger({LK.CARD_NAME: self.name})

    def debug_str(self) -> str:
        """ Returns a string describing this card. """
        # TODO -> consider adding 'name_only' argument.
        return self.name

    def get_descriptor_for_minimal_printing(self) -> str:
        """ Returns the minimal descriptor to explain this card. """
        return f"{self.name} ({self.card_type.value.title()}): {self.text}"
