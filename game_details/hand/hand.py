""" Hand class """
from dataclasses import dataclass

from game_details.card import Card, MultipleCardsHolder


@dataclass
class Hand(MultipleCardsHolder):

    limit: int = 7

    @staticmethod
    def create_default() -> 'Hand':
        """ Creates a hand with an empty list. """
        return Hand(cards=[])

    def add_card(self, card: Card) -> None:
        """ Adds the given card to this hand. """
        self.cards.append(card)

    def must_discard_to_limit(self) -> bool:
        """ Returns whether the hand has more cards than the limit """
        return self.limit < len(self)

    def choose_card_to_discard(self) -> Card | None:
        """ Handles the process of choosing a card to discard from this hand. Will continue until a valid card to
        remove has been chosen, and returns it. """
        self.print_basics_with_index()

        # Exit early if there's no cards.
        if len(self) == 0:
            return None

        valid_numbers = [str(i + 1) for i in range(len(self))]
        prompt = f"Choose ({'|'.join(valid_numbers)}): "
        response = input(prompt)  # Would rather not deal with an exception, so convert to int later.
        while response not in valid_numbers:
            print(f"Could not understand {response}, please try again.")
            response = input(prompt)

        chosen_card = self[int(response) - 1]
        self.remove(chosen_card)
        return chosen_card

    def print_basics_with_index(self) -> None:
        """ Print the basic card info with an index. """
        if len(self) == 0:
            print("You have no cards.")
            return

        for index, card in enumerate(self.cards):
            print(f"[{index + 1}]\t{card.get_descriptor_for_minimal_printing()}")
