""" Factory for creating Effect instances. """
from game_details.card.effect import Effect, EffectTrigger


def create_default() -> Effect:
    """ Creates a default effect. """
    return Effect()


def create(card_info: dict) -> Effect:
    """ Creates an effect from the given dictionary. Passed the full card dict to check if it actually exists. """
    if "effect" in card_info:
        return Effect(EffectTrigger.create(card_info["effect"]["trigger"]))
    return Effect()
