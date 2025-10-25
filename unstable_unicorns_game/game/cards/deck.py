""" Deck class """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_stack import CardStack


@dataclass
class Deck(CardStack):
    """ Manages interactions with the current deck. """

    @classmethod
    def create_default(cls) -> Deck:
        """ Creates a deck with no cards. """
        return Deck(cards=[])

    @classmethod
    def create_one_card(cls, card: Card) -> Deck:
        """ Creates a deck containing the given card. """
        return Deck(cards=[card])

    @classmethod
    def create(cls, cards: list[Card], *args, **kwargs) -> Deck:
        """ Creates a deck containing the given list of card. """
        return Deck(cards)

    def draw_top(self) -> Card:
        """ Removes and returns the top (first) card from this pile."""
        return self.pop_top()
