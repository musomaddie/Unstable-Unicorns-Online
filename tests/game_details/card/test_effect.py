from game_details.card.effect import Effect, EffectTrigger


class TestConstructor:

    def test_create_effect(self):
        effect = Effect(EffectTrigger.EVENT)
        assert effect.trigger == EffectTrigger.EVENT
