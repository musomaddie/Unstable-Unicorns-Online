""" An enum for the card type. """
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

    @staticmethod
    def create_default() -> 'CardType':
        """ Creates a default card type. """
        return CardType.BASIC_UNICORN
