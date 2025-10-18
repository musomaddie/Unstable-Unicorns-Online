""" File for card stuff """
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.card_type import CardType
from unstable_unicorns_game.game_details.card.effect.effect import Effect


@dataclass
class Card(metaclass=ABCMeta):
    """ Class for holding information about a card within the deck. """

    name: str
    card_type: CardType
    text: str
    effect: Effect

    @abstractmethod
    def get_descriptor_for_minimal_printing(self) -> str:
        """ Returns the minimal descriptor to explain this card. """
        pass
