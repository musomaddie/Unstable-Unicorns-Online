""" Cards stuff. """
from dataclasses import dataclass

from game_details.card import Card


@dataclass
class MultipleCardsHolder:
    """ Super class for anything that contains multiple cards. Basically simple helpers."""

    cards: list[Card]

    def __len__(self):
        return len(self.cards)

    def __iter__(self) -> 'MultipleCardsIterator':
        return MultipleCardsIterator(self)

    def __getitem__(self, item) -> Card:
        return self.cards[item]

    def __contains__(self, item) -> bool:
        return item in self.cards

    def __add__(self, other: 'MultipleCardsHolder'):
        return MultipleCardsHolder(self.cards + other.cards)

    def remove(self, card: Card) -> None:
        """ Removes the given card from this holder. Throws ValueError if the card does not exist."""
        if card not in self:
            raise ValueError(f"{card} not found within {self}.")
        self.cards.remove(card)


class MultipleCardsIterator:
    """ An interator for something that contains multiple cards. """

    def __init__(self, cards: MultipleCardsHolder):
        self._cards = cards
        self._index = 0

    def __next__(self) -> Card:
        if self._index < len(self._cards):
            self._index += 1
            return self._cards[self._index - 1]
        raise StopIteration
