""" Tests for the Effect class  TODO - figure out how to link this"""
from game_details.card.effect import Effect, EffectTrigger


class TestCreate:

    def test_create_effect_default(self):
        effect = Effect()
        assert effect.trigger == EffectTrigger.NONE

    def test_create_effect_empty_dict(self):
        effect = Effect.create({})

    def test_
