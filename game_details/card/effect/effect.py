""" Effect"""
from dataclasses import dataclass

from game_details.card.effect.effect_trigger import EffectTrigger


@dataclass
class Effect:
    """ Class to manage card effects. """
    trigger: EffectTrigger = EffectTrigger.create_default()

    @staticmethod
    def create_default() -> 'Effect':
        """ Creates a default effect. """
        return Effect()

    @staticmethod
    def create(card_info: dict) -> 'Effect':
        """ Creates an effect from the given dictionary. Passed the full card dict to check if it actually exists. """
        if "effect" in card_info:
            return Effect(EffectTrigger.create(card_info["effect"]["trigger"]))
        return Effect()
