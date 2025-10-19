""" File for card stuff """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.card.card_type import CardType
from unstable_unicorns_game.game.card.effect.effect import Effect


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

    def get_descriptor_for_minimal_printing(self) -> str:
        """ Returns the minimal descriptor to explain this card. """
        return f"{self.name} ({self.card_type.value.title()}): {self.text}"
