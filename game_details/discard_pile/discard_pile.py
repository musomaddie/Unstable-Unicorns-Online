from dataclasses import dataclass

from game_details.card import CardStack


@dataclass
class DiscardPile(CardStack):
    """ A manager for the discard pile."""
