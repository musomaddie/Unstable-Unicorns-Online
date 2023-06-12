from dataclasses import dataclass, field

from game_details.card import Card


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)

    def __len__(self):
        return len(self.cards)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
