""" Cards stuff. """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.utilities.logger import Logger


@dataclass
class MultipleCardsHolder:
    """ Super class for anything that contains multiple cards. Basically simple helpers."""

    cards: list[Card]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        yield from self.cards

    def __getitem__(self, item) -> Card:
        return self.cards[item]

    def __contains__(self, item) -> bool:
        return item in self.cards

    def __add__(self, other: 'MultipleCardsHolder'):
        return MultipleCardsHolder(self.cards + other.cards)

    @classmethod
    def create(cls, cards: list[Card], *args, **kwargs) -> MultipleCardsHolder:
        """ Creates a cardholder with the given cards. """
        # Using *args and **kwargs to allow for future expansion (Liskov substitution principle).
        return cls(cards)

    @classmethod
    def create_default(cls) -> MultipleCardsHolder:
        return cls(cards=[])

    @classmethod
    def create_with_one_card(cls, card: Card) -> MultipleCardsHolder:
        return cls(cards=[card])

    def log_all(self) -> list[Logger]:
        """ Returns a list of log information for all cards in this holder."""
        return [card.log() for card in self]

    def debug_str(self, include_size: bool = False, list_all: bool = False) -> str:
        """ Returns a string (possibly multi-line) describing the current state of the cards.

        Some arguments will mean others are ignored.
        # TODO -> pydoc -> how to consistently format this?
        """
        result = ""
        if list_all:
            result = ", ".join([card.debug_str() for card in self])
            pass
        if include_size:
            if len(result) == 0:
                result = f"{len(self)} cards"
            else:
                result = f"{result} |{len(self)}|"
        return result

    def get_card_indices_for_display(self):
        return [str(i + 1) for i in range(len(self))]

    def get_card_from_display_index(self, display_index: str) -> Card:
        return self[int(display_index) - 1]

    def remove(self, card: Card) -> None:
        """ Removes the given card from this holder. Throws ValueError if the card does not exist."""
        if card not in self:
            raise ValueError(f"{card} not found within {self}.")
        self.cards.remove(card)
