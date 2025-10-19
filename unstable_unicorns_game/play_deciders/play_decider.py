""" container for all parent decider classes. """
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from unstable_unicorns_game.game_details.hand.hand import Hand
from unstable_unicorns_game.game_details.card.card import Card


class PlayDecider(ABC):
    """ Abstract class which defines the methods all play deciders must include. """

    @abstractmethod
    def choose_discard(self, hand: Hand) -> Optional[Card]:
        """ Returns the card which should be discarded, or none if the hand contains no cards. """
        pass
