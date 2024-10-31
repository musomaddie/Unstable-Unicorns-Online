""" CARD. """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.card import Card


@dataclass
class CardImpl(Card):
    """Implementation of card. """

    def get_descriptor_for_minimal_printing(self) -> str:
        return f"{self.name} ({self.card_type.value.title()}): {self.text}"
