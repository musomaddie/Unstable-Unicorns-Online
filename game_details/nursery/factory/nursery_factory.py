""" Factory for creating Nursery instances. """
from game_details.card import CardType
from game_details.card.factory import card_factory
from game_details.nursery import Nursery
from game_details.nursery.impl.nursery_impl import NurseryImpl


def create_default() -> Nursery:
    """ Creates a nursery with 25 identical children. """
    return NurseryImpl(
        cards=[card_factory.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])
