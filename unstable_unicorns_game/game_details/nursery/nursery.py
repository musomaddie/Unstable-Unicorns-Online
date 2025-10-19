""" Nursery class file """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_stack import CardStack
from unstable_unicorns_game.game_details.card.card_type import CardType


@dataclass
class Nursery(CardStack):
    """ Managers the nursery. """
    cards: list[Card]

    @classmethod
    def create_default(cls) -> Nursery:
        """ Creates a nursery with 25 identical children. """
        return cls(
            cards=[Card.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])

    def get_baby(self) -> Card:
        """ Removes and returns the first baby from the nursery. """
        return self.pop_top()
