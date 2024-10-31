""" Discard Pile """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import CardStack


@dataclass
class DiscardPile(CardStack):
    """ A manager for the discard pile."""
