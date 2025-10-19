from dataclasses import dataclass
from typing import Optional

from unstable_unicorns_game.game.card.card import Card
from unstable_unicorns_game.game.hand.hand import Hand
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


@dataclass
class TestDecider(PlayDecider):
    """ A play decider which should be used only within tests, it makes decisions in the order passed to it."""
    decisions: list[str]

    def choose_discard(self, hand: Hand) -> Optional[Card]:
        # Exit early if there are no cards to discard.
        if len(hand) == 0:
            return None

        # Don't bother error checking, it's for tests we can be a bit hacky.
        return hand.get_card_from_display_index(self.decisions.pop(0))
