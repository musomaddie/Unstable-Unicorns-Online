from dataclasses import dataclass

from game_details.card import Card


@dataclass
class Nursery:
    babies: list[Card]
