from dataclass import dataclass, field

from game_details.card import Card


@dataclass
class CardStack:
    """ A super class for managing anything that is a pile of cards (e.g. deck, discard pile). """

    cards: list[Card] = field(default_factory=list)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]

    def draw_top(self):
        """ Removes and returns the top (first) card from this pile."""
        return self.cards.pop(0)
