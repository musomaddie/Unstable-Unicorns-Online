""" An enum for the card type. """
from __future__ import annotations

from enum import Enum


class CardType(Enum):
    """ Represents the possible types of cards. """
    BABY_UNICORN = "baby unicorn"
    BASIC_UNICORN = "basic unicorn"
    DOWNGRADE = "downgrade"
    INSTANT = "instant"
    MAGIC = "magic"
    MAGIC_UNICORN = "magic unicorn"
    UPGRADE = "upgrade"

    @classmethod
    def create_default(cls) -> CardType:
        """ Creates a default card type. """
        return CardType.BASIC_UNICORN

    @classmethod
    def create(cls, name: str) -> CardType:
        """ Creates a card type from the given name. """
        for enum in cls:
            if enum.value == name:
                return enum
        raise ValueError(f"Invalid card type: {name}")

    def play_to_stable(self) -> bool:
        return self in (
            CardType.MAGIC_UNICORN, CardType.BASIC_UNICORN, CardType.BABY_UNICORN, CardType.DOWNGRADE, CardType.UPGRADE)
