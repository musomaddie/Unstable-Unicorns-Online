from enum import Enum


class CardType(Enum):
    """ Represents the possible types of cards. """
    MAGIC = "magic"
    MAGIC_UNICORN = "magic unicorn"
    BASIC_UNICORN = "basic unicorn"
    UPGRADE = "upgrade"
    DOWNGRADE = "downgrade"
    INSTANT = "instant"
