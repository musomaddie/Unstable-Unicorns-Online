""" Implementation of hand. """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card import Card
from unstable_unicorns_game.game_details.hand import Hand
from unstable_unicorns_game.play_deciders.play_decider import DiscardDecider


@dataclass
class HandImpl(Hand):
    """ Implementation of Hand."""

    decider: DiscardDecider = None

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def must_discard_to_limit(self) -> bool:
        return self.limit < len(self)

    def print_basics_with_index(self) -> None:
        if len(self) == 0:
            print("You have no cards.")
            return

        for index, card in enumerate(self.cards):
            print(f"[{index + 1}]\t{card.get_descriptor_for_minimal_printing()}")

    def choose_card_to_discard(self) -> Card | None:
        if self.decider is None:
            raise TypeError("Attempting to make a decision without a play decider.")

        # Exit early if there's no cards.
        if len(self) == 0:
            return None

        chosen_card = self.decider.decide_discard()
        self.remove(chosen_card)
        return chosen_card
