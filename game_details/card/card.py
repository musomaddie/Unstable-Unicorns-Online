import dataclasses
import json

from game_details.card.card_type import CardType


@dataclasses.dataclass
class Card:
    """ Class for holding information about a card within the deck. """

    name: str
    card_type: CardType
    card_text: str

    @staticmethod
    def create_card(card_info: dict) -> 'Card':
        return Card(card_info["name"], CardType(card_info["type"]), card_info["text"])

    @staticmethod
    def create_all_cards() -> list['Card']:
        """ Creates card objects for every card within the json file. """
        file_contents = json.load(open("db/card_details.json"))
        return [Card.create_card(card_info) for card_info in file_contents]


if __name__ == '__main__':
    print(Card.create_all_cards())
