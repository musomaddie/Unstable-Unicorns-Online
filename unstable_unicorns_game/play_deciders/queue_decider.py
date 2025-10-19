from __future__ import annotations

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from unstable_unicorns_game.game.hand.hand import Hand

from unstable_unicorns_game.game.card.card import Card
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


class QueueDecider(PlayDecider):
    """
    A play decider which functions as a queue -> first in first out data structure.
    """

    def choose_discard(self, hand: Hand) -> Optional[Card]:
        if len(hand) == 0:
            return None
        return hand.cards[0]
