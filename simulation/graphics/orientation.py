""" orientation enum """
from enum import Enum, auto


class Orientation(Enum):
    """ Represents which way a particular class is orientated. """
    VERTICAL = auto()  # UP / DOWN axis in the long side.
    HORIZONTAL = auto()  # LEFT / RIGHT axis is the  is long side
