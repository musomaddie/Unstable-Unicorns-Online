""" Effect"""
from dataclasses import dataclass

from unstable_unicorns_game.game.card.effect.effect_trigger import EffectTrigger


@dataclass
class Effect:
    """ Class to manage card effects. """
    trigger: EffectTrigger

    @classmethod
    def create_default(cls) -> 'Effect':
        """ Creates a default effect. """
        return cls(EffectTrigger.create_default())

    @classmethod
    def create(cls, card_info: dict) -> 'Effect':
        """ Creates an effect from the given dictionary. Passed the full card dict to check if it actually exists. """
        if "effect" in card_info and "trigger" in card_info["effect"]:
            return cls(EffectTrigger.create(card_info["effect"]["trigger"]))
        return cls.create_default()
