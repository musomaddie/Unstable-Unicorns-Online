from dataclasses import dataclass, field

from game_details.card import Card, CardType, CardStack


@dataclass
class Nursery(CardStack):
    """ Managers the nursery. """
    cards: list[Card] = field(
        default_factory=lambda: [Card("Baby Unicorn", CardType.BABY_UNICORN, "text") for _ in range(25)])

    def get_baby(self):
        """ Removes and returns the first baby from the nursery. """
        return self.pop_top()
