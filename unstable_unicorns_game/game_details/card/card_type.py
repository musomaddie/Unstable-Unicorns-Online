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
