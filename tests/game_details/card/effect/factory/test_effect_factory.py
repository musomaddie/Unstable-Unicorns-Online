""" Tests for the Effect class  TODO - figure out how to link this"""
from unstable_unicorns_game.game_details.card.effect import EffectTrigger
from unstable_unicorns_game.game_details.card.effect.factory import effect_factory


class TestCreate:

    def test_create_effect_default(self):
        effect = effect_factory.create_default()
        assert effect.trigger == EffectTrigger.NONE

    def test_create_effect_empty_dict(self):
        effect = effect_factory.create({})
        assert effect.trigger == EffectTrigger.NONE
