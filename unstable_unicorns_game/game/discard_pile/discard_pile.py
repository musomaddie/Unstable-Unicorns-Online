""" Discard Pile """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.card.card import Card
from unstable_unicorns_game.game.card.card_stack import CardStack


@dataclass
class DiscardPile(CardStack):
    """ A manager for the discard pile."""

    @classmethod
    def create_default(cls) -> DiscardPile:
        """ Creates a discard pile with no cards. """
        return cls(cards=[])

    @classmethod
    def create(cls, cards: list[Card]) -> DiscardPile:
        return cls(cards)
