""" Hand class """
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.play_deciders.discard_decider import DiscardDecider
from unstable_unicorns_game.play_deciders.factory import decider_factory
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


@dataclass
class Hand(MultipleCardsHolder):

    limit: int = 7
    # TODO -> figure out a better way to set this.
    decider: DiscardDecider = None

    @classmethod
    def create(cls, cards: list[Card], decider: Optional[PlayDecider] = None) -> Hand:
        """ Creates a hand containing the given cards. """
        # TODO -> modify this to not take in a list of cards. Makes sense to create an empty hand which is progressively
        #  added to. (or otherwise use a builder).
        hand = cls(cards)
        if decider is None:
            hand.decider = decider_factory.create("queue").create_discard_decider(hand)
        else:
            hand.decider = decider.create_discard_decider(hand)
        return hand

    @classmethod
    def create_default(cls) -> Hand:
        return cls.create(cards=[])

    def add_card(self, card: Card) -> None:
        """ Adds the given card to this hand. """
        self.cards.append(card)

    def must_discard_to_limit(self) -> bool:
        """ Returns whether the hand has more cards than the limit """
        return self.limit < len(self)

    def choose_card_to_discard(self) -> Card | None:
        """ Handles the process of choosing a card to discard from this hand. Will continue until a valid card to
        remove has been chosen and returns it. """
        if self.decider is None:
            raise TypeError("Attempting to make a decision without a play decider.")

        # Exit early if there is no cards.
        if len(self) == 0:
            return None

        chosen_card = self.decider.decide()
        self.remove(chosen_card)
        return chosen_card

    def print_basics_with_index(self) -> None:
        """ Print the basic card info with an index. """
        if len(self) == 0:
            print("You have no cards.")
            return

        for index, card in enumerate(self.cards):
            print(f"[{index + 1}]\t{card.get_descriptor_for_minimal_printing()}")
