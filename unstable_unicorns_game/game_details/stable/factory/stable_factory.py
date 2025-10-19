""" Factory for creating Stable instances. """
from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_type import CardType
from unstable_unicorns_game.game_details.card.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game_details.stable import Stable


def create_default() -> Stable:
    """ Create a default stable. """
    return Stable(
        unicorns=MultipleCardsHolder.create_with_one_card(Card.create_default("Baby Unicorn", CardType.BABY_UNICORN)),
        upgrades=MultipleCardsHolder.create_default(),
        downgrades=MultipleCardsHolder.create_default())


def create(baby_unicorn) -> Stable:
    """ Creates a stable containing only the given baby unicorn. """
    return Stable(
        unicorns=MultipleCardsHolder.create_with_one_card(baby_unicorn),
        upgrades=MultipleCardsHolder.create_default(),
        downgrades=MultipleCardsHolder.create_default())
