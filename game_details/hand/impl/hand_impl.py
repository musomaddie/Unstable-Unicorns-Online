""" Implementation of hand. """
from game_details.card import Card
from game_details.hand import Hand


class HandImpl(Hand):
    """ Implementation of Hand."""

    def connect_play_decider(self, play_decider: 'PlayDecider'):
        self.play_decider = play_decider

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
        if self.play_decider is None:
            raise TypeError("Attempting to make a decision without a play decider.")

        # Exit early if there's no cards.
        if len(self) == 0:
            return None

        chosen_card = self.play_decider.decide_discard()
        self.remove(chosen_card)
        return chosen_card
