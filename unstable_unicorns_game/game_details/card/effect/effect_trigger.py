""" Effect trigger. """
from enum import Enum


class EffectTrigger(Enum):
    """ The options corresponding to when a card effect can actually be triggered."""
    ENTERS_STABLE = "enters stable"
    NONE = "none"
