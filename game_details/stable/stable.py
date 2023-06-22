from dataclasses import dataclass, field

from game_details.card import Card, CardType, MultipleCardsHolder


@dataclass
class Stable:
    """ Represents a stable."""
    # TODO - replace the baby unicorn with an actual one.
    unicorns: MultipleCardsHolder = field(default_factory=lambda: [Card("Baby Unicorn", CardType.BABY_UNICORN, "text")])
    upgrades: MultipleCardsHolder = field(default_factory=list)
    downgrades: MultipleCardsHolder = field(default_factory=list)
