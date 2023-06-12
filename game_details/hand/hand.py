from dataclasses import dataclass, field

from game_details.card.card import Card


@dataclass
class Hand:
    cards: list[Card] = field(default_factory=list)
