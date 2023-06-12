from dataclasses import dataclass, field

from game_details.card import Card


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return HandIterator(self)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)


class HandIterator:
    """ An iterator for the hand, goes through and returns each card."""

    def __init__(self, hand: Hand):
        self._hand = hand
        self._index = 0

    def __next__(self):
        if self._index < len(self._hand):
            self._index += 1
            return self._hand.cards[self._index - 1]
        raise StopIteration
