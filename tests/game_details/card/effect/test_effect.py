import pytest

from unstable_unicorns_game.game_details.card.effect.effect import Effect
from unstable_unicorns_game.game_details.card.effect.effect_trigger import EffectTrigger


class TestCreateDefault:
    def test_create_default_returns_none_trigger(self):
        effect = Effect.create_default()
        assert effect.trigger == EffectTrigger.NONE


class TestCreate:
    @pytest.mark.parametrize(
        ("trigger_value", "expected_trigger"),
        [
            ("enters stable", EffectTrigger.ENTERS_STABLE),
            ("none", EffectTrigger.NONE)
        ]
    )
    def test_create_with_valid_trigger(self, trigger_value, expected_trigger):
        card_info = {"effect": {"trigger": {"event": trigger_value}}}
        effect = Effect.create(card_info)
        assert effect.trigger == expected_trigger

    def test_create_missing_effect_key(self):
        effect = Effect.create({})
        assert effect.trigger == EffectTrigger.NONE

    def test_create_with_empty_effect_dict(self):
        card_info = {"effect": {}}
        effect = Effect.create(card_info)
        assert effect.trigger == EffectTrigger.NONE

    def test_create_with_invalid_trigger(self):
        card_info = {"effect": {"trigger": {"event": "invalid_trigger"}}}
        effect = Effect.create(card_info)
        assert effect.trigger == EffectTrigger.NONE

    def test_create_with_missing_trigger_key(self):
        card_info = {"effect": {"other_key": "value"}}
        effect = Effect.create(card_info)
        assert effect.trigger == EffectTrigger.NONE

    def test_create_with_empty_event_string(self):
        card_info = {"effect": {"trigger": {"event": ""}}}
        effect = Effect.create(card_info)
        assert effect.trigger == EffectTrigger.NONE
