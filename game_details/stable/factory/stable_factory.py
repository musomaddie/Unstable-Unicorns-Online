""" Factory for creating Stable instances. """
from game_details.card import MultipleCardsHolder, CardType
from game_details.card.factory import card_factory
from game_details.stable import Stable


def create_default() -> Stable:
    """ Create a default stable. """
    return Stable(
        unicorns=MultipleCardsHolder.create(card_factory.create_default("Baby Unicorn", CardType.BABY_UNICORN)),
        upgrades=MultipleCardsHolder.create_default(),
        downgrades=MultipleCardsHolder.create_default())


def create(baby_unicorn) -> Stable:
    """ Creates a stable containing only the given baby unicorn. """
    return Stable(
        unicorns=MultipleCardsHolder.create(baby_unicorn),
        upgrades=MultipleCardsHolder.create_default(),
        downgrades=MultipleCardsHolder.create_default())
