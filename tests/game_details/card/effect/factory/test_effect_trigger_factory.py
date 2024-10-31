""" tests for effect trigger. """
import pytest

from game_details.card.effect import EffectTrigger
from game_details.card.effect.factory import effect_trigger_factory


class TestCreate:

    @pytest.mark.parametrize(
        ("input_text", "expected_result"),
        [("enters stable", EffectTrigger.ENTERS_STABLE), ("none", EffectTrigger.NONE)])
    def test_create_corresponding_text(self, input_text, expected_result):
        effect_trigger = effect_trigger_factory.create({"event": input_text})
        assert effect_trigger == expected_result

    def test_create_missing_dict_key(self):
        effect_trigger = effect_trigger_factory.create({})
        assert effect_trigger == EffectTrigger.NONE

    def test_create_spam_text(self):
        effect_trigger = effect_trigger_factory.create({"event": "adkfja;djfkl"})
        assert effect_trigger == EffectTrigger.NONE


def test_create_default():
    effect_trigger = effect_trigger_factory.create_default()
    assert effect_trigger == EffectTrigger.NONE
