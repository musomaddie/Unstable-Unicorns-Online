""" Factory for creating Effect instances. """
from game_details.card.effect import Effect
from game_details.card.effect.factory import effect_trigger_factory


def create_default() -> Effect:
    """ Creates a default effect. """
    return Effect(effect_trigger_factory.create_default())


def create(card_info: dict) -> Effect:
    """ Creates an effect from the given dictionary. Passed the full card dict to check if it actually exists. """
    if "effect" in card_info:
        return Effect(effect_trigger_factory.create(card_info["effect"]["trigger"]))
    return create_default()
