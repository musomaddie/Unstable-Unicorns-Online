""" Hand class """
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider
from unstable_unicorns_game.play_deciders.queue_decider import QueueDecider


@dataclass
class Hand(MultipleCardsHolder):
    decider: PlayDecider
    limit: int = 7

    @classmethod
    def create(cls, cards: list[Card], decider: PlayDecider = QueueDecider(), *args, **kwargs) -> Hand:
        """ Creates a hand containing the given cards. """
        return cls(cards, decider)

    @classmethod
    def create_default(cls) -> Hand:
        return cls.create(cards=[])

    def debug_str(self, indents: int = 0, **kwargs) -> str:
        text = f"{'Hand' :<15} : {super().debug_str(list_all=True)}"
        return f"{'\t' * indents}{text}"

    def add_card(self, card: Card) -> None:
        """ Adds the given card to this hand. """
        self.cards.append(card)

    def must_discard_to_limit(self) -> bool:
        """ Returns whether the hand has more cards than the limit """
        return self.limit < len(self)

    def discard(self) -> Optional[Card]:
        """ Discards a card from this hand (unless there are none to discard). """
        # I'm unsure this decider pattern will be compatibile with the GUI.
        card = self.decider.choose_discard(self)
        if card is not None:
            self.remove(card)
        return card

    def print_basics_with_index(self) -> None:
        """ Print the basic card info with an index. """
        if len(self) == 0:
            print("You have no cards.")
            return

        for index, card in enumerate(self.cards):
            print(f"[{index + 1}]\t{card.get_descriptor_for_minimal_printing()}")
