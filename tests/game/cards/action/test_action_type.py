import pytest

from unstable_unicorns_game.game.cards.action.action_type import ActionType


class TestCreate:
    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [("steal", ActionType.STEAL)]
    )
    def test_create_corresponding_type(self, input_string, expected_result):
        assert ActionType.create_from_dict({"action_type": input_string}) == expected_result

    def test_create_missing_dict_key(self):
        assert ActionType.create_from_dict({}) == ActionType.NONE

    def test_create_spam(self):
        assert ActionType.create_from_dict({"action_type": "adfjkdl;afj"}) == ActionType.NONE
