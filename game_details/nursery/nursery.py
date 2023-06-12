from dataclasses import dataclass, field

from game_details.card import Card, CardType


@dataclass
class Nursery:
    babies: list[Card] = field(
        default_factory=lambda: [Card("Baby Unicorn", CardType.BABY_UNICORN, "text") for _ in range(25)])
