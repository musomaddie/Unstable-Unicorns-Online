from dataclasses import dataclass

from game_details.card import Card, MultipleCardsHolder


@dataclass
class Hand(MultipleCardsHolder):

    limit: int = 7

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def must_discard_to_limit(self) -> bool:
        return self.limit <= len(self)

    def print_basics_with_index(self):
        if len(self) == 0:
            print("You have no cards.")
            return

        for index, card in enumerate(self.cards):
            print(f"[{index}]\t{card.get_descriptor_for_minimal_printing()}")
