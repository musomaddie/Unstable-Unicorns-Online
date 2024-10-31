""" Effect"""
from dataclasses import dataclass

from game_details.card.effect.effect_trigger import EffectTrigger


@dataclass
class Effect:
    """ Class to manage card effects. """
    trigger: EffectTrigger
