""" Nursery class file """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_stack import CardStack
from unstable_unicorns_game.game.cards.card_type import CardType


@dataclass
class Nursery(CardStack):
    """ Managers the nursery. """
    cards: list[Card]

    @classmethod
    def create_default(cls) -> Nursery:
        """ Creates a nursery with 25 identical children. """
        return cls(
            cards=[Card.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])

    def debug_str(self, **kwargs) -> str:
        return f"{'Nursery':<8} : {super().debug_str(include_size=True)}"

    def get_baby(self) -> Card:
        """ Removes and returns the first baby from the nursery. """
        return self.pop_top()
