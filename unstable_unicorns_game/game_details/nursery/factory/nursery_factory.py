""" Factory for creating Nursery instances. """
from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_type import CardType
from unstable_unicorns_game.game_details.nursery import Nursery
from unstable_unicorns_game.game_details.nursery.impl.nursery_impl import NurseryImpl


def create_default() -> Nursery:
    """ Creates a nursery with 25 identical children. """
    return NurseryImpl(
        cards=[Card.create_default("Baby Unicorn", CardType.BABY_UNICORN) for _ in range(25)])
