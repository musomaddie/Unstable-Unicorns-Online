from enum import Enum


class CardLocation(Enum):
    DECK = 1
    HAND = 2
    STABLE = 3
    DISCARD_PILE = 4
    # TODO: not going to be nice for nursery :(
