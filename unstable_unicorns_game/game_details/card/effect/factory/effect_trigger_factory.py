""" Factory for creating EffectTrigger instances. """
from unstable_unicorns_game.game_details.card.effect import EffectTrigger


def create_default() -> EffectTrigger:
    """ Returns a default value for this class. """
    return EffectTrigger.NONE


def create(trigger_info: dict) -> EffectTrigger:
    """ Creates a trigger info from the given dictionary. """
    if "event" not in trigger_info:
        return create_default()
    desc = trigger_info["event"]
    for enum in EffectTrigger:
        if enum.value == desc:
            return enum
    return create_default()
