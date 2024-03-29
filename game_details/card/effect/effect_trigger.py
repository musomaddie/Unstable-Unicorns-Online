""" Effect trigger. """
from enum import Enum


class EffectTrigger(Enum):
    """ The options corresponding to when a card effect can actually be triggered."""
    ENTERS_STABLE = "enters stable"
    NONE = "none"

    @staticmethod
    def create_default() -> 'EffectTrigger':
        """ Returns a default value for this class. """
        return EffectTrigger.NONE

    @staticmethod
    def create(trigger_info: dict) -> 'EffectTrigger':
        """ Creates a trigger info from the given dictionary. """
        if "event" not in trigger_info:
            return EffectTrigger.create_default()
        desc = trigger_info["event"]
        for enum in EffectTrigger:
            if enum.value == desc:
                return enum
        return EffectTrigger.create_default()
