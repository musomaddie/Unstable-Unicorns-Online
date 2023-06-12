from dataclasses import dataclass

from game_details.card.card import Card


@dataclass
class Nursery:
    babies: list[Card]
