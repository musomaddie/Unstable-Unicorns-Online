""" Effect trigger. """
from enum import Enum


class EffectTrigger(Enum):
    """ The options corresponding to when a card effect can actually be triggered."""
    ENTERS_STABLE = "enters stable"
    NONE = "none"

    @classmethod
    def create_default(cls) -> 'EffectTrigger':
        """ Returns a default value for this class. """
        return cls.NONE

    @classmethod
    def create(cls, trigger_info: dict) -> 'EffectTrigger':
        """ Creates a trigger info from the given dictionary. """
        if "event" not in trigger_info:
            return cls.create_default()
        desc = trigger_info["event"]
        for enum in cls:
            if enum.value == desc:
                return enum
        return cls.create_default()
