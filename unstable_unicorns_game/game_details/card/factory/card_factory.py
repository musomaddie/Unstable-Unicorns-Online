""" card factory. """
import json

from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_type import CardType
from unstable_unicorns_game.game_details.card.effect.factory import effect_factory
from unstable_unicorns_game.game_details.card.impl.card_impl import CardImpl as Impl


def create_default(name: str, card_type: CardType) -> Card:
    """ Creates a card from the given type and name. """
    return Impl(name, card_type, "default text", effect_factory.create_default())


def create(card_info: dict) -> Card:
    """ Creates a card from the given dictionary. """
    return Impl(
        card_info["name"],
        CardType(card_info["type"]),
        card_info["text"],
        effect_factory.create(card_info))


def create_all() -> list['Card']:
    """ Creates card objects for every card within the json file. """
    file_contents = json.load(open("unstable_unicorns_game/data/card_details.json"))
    # TODO - temporary for testing, delete this later!!
    cards = [create(card_info) for card_info in file_contents]
    while len(cards) < 30:
        cards.append(cards[0])
    return cards
