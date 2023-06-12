from dataclasses import dataclass, field

from game_details.card.card import Card
from game_details.card.card_type import CardType


@dataclass
class Stable:
    """ Represents a stable."""
    # TODO - replace the baby unicorn with an actual one.
    unicorns: list[Card] = field(default_factory=lambda: [Card("Baby Unicorn", CardType.BABY_UNICORN, "text")])
    upgrades: list[Card] = field(default_factory=list)
    downgrades: list[Card] = field(default_factory=list)
