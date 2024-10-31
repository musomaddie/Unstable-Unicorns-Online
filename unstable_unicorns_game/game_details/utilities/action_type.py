""" action type """

from enum import Enum, auto


class TurnActionType(Enum):
    DRAW_CARD = auto()
    PLAY_CARD = auto()
