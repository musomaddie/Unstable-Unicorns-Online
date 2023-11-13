from dataclasses import dataclass
from enum import Enum


@dataclass
class Effect:
    """ Class to manage card effects. """
    trigger: str


class EffectTrigger(Enum):
    """ The options corresponding to when a card effect can actually be triggered."""
    EVENT = "event"
