from dataclasses import dataclass

from game_details.card import Card


@dataclass
class Hand:
    cards: list[Card]
