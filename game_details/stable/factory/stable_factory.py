""" Factory for creating Stable instances. """
from game_details.card import CardType
from game_details.card.factory import multiple_cards_factory, card_factory
from game_details.stable import Stable


def create_default() -> Stable:
    """ Create a default stable. """
    return Stable(
        unicorns=multiple_cards_factory.create(card_factory.create_default("Baby Unicorn", CardType.BABY_UNICORN)),
        upgrades=multiple_cards_factory.create_default(),
        downgrades=multiple_cards_factory.create_default())


def create(baby_unicorn) -> Stable:
    """ Creates a stable containing only the given baby unicorn. """
    return Stable(
        unicorns=multiple_cards_factory.create(baby_unicorn),
        upgrades=multiple_cards_factory.create_default(),
        downgrades=multiple_cards_factory.create_default())
