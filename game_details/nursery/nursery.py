""" Nursery class file """
from dataclasses import dataclass

from game_details.card import Card, CardType, CardStack


@dataclass
class Nursery(CardStack):
    """ Managers the nursery. """
    cards: list[Card]

    @staticmethod
    def create_default() -> 'Nursery':
        """ Creates a nursery with 25 identical children. """
        return Nursery(
            cards=[Card.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])

    def get_baby(self) -> Card:
        """ Removes and returns the first baby from the nursery. """
        return self.pop_top()
