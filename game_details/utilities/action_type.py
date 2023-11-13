""" action type """

from enum import Enum, auto


class ActionType(Enum):
    DRAW_CARD = auto()
    PLAY_CARD = auto()
