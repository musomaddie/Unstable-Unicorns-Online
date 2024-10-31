""" action type"""
from enum import Enum


class ActionType(Enum):
    """ The type of action. """
    STEAL = "steal"
    NONE = "none"
