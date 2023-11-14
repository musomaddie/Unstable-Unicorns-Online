""" tests for action type """
import pytest

from game_details.card.action import ActionType


class TestCreate:

    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [("steal", ActionType.STEAL), ("none", ActionType.NONE)])
    def test_create_corresponding_string(self, input_string, expected_result):
        action_type = ActionType.create({"action_type": input_string})
        assert action_type == expected_result

    def test_create_missing_dict_key(self):
        assert ActionType.create({}) == ActionType.NONE

    def test_create_spam(self):
        assert ActionType.create({"action_type": "adfjkdl;afj"}) == ActionType.NONE
