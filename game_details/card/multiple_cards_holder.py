from dataclasses import dataclass, field

from game_details.card import Card


@dataclass
class MultipleCardsHolder:
    """ Super class for anything that contains multiple cards. Basically simple helpers."""

    cards: list[Card] = field(default_factory=list)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return MultipleCardsIterator(self)

    def __getitem__(self, item):
        return self.cards[item]

    def __contains__(self, item):
        return item in self.cards

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

    def __next__(self):
        if self._index < len(self._cards):
            self._index += 1
            return self._cards[self._index - 1]
        raise StopIteration
