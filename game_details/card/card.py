""" File for card stuff """
import json
from dataclasses import dataclass

from game_details.card.card_type import CardType
from game_details.card.effect import Effect


@dataclass
class Card:
    """ Class for holding information about a card within the deck. """

    name: str
    card_type: CardType
    text: str
    effect: Effect

    @staticmethod
    def create_default(name: str, card_type: CardType) -> 'Card':
        """ Creates a card from the given type. """
        return Card(name, card_type, "default text", Effect.create_default())

    @staticmethod
    def create_card(card_info: dict) -> 'Card':
        """ Creates a Card object from the given dictionary. """
        return Card(
            card_info["name"],
            CardType(card_info["type"]),
            card_info["text"],
            Effect.create(card_info))

    @staticmethod
    def create_all_cards() -> list['Card']:
        """ Creates card objects for every card within the json file. """
        file_contents = json.load(open("db/card_details.json"))
        # TODO - temporary for testing, delete this later!!
        cards = [Card.create_card(card_info) for card_info in file_contents]
        while len(cards) < 30:
            cards.append(cards[0])
        return cards

    def get_descriptor_for_minimal_printing(self) -> str:
        """ Returns the minimal descriptor to explain this card. """
        return f"{self.name} ({self.card_type.value.title()}): {self.text}"


if __name__ == '__main__':
    print(Card.create_all_cards())
