""" Factory for creating Nursery instances. """
from unstable_unicorns_game.game_details.card import CardType
from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.nursery import Nursery
from unstable_unicorns_game.game_details.nursery.impl.nursery_impl import NurseryImpl


def create_default() -> Nursery:
    """ Creates a nursery with 25 identical children. """
    return NurseryImpl(
        cards=[card_factory.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])
