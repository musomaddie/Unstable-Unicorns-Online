from dataclasses import dataclass

from game_details.card import Card, MultipleCardsHolder


@dataclass
class Hand(MultipleCardsHolder):

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
