""" test for action """
import pytest

from game_details.card.action import Action, ActionType


def test_create_default():
    action = Action.create_default()
    assert action.create_default()


class TestCreate:

    @pytest.mark.parametrize(
        ("action_type_str", "expected_action_type"),
        [("steal", ActionType.STEAL), ("none", ActionType.NONE)])
    def test_with_dict_action_type(self, action_type_str, expected_action_type):
        action = Action.create({"action": {"action_type": action_type_str}})
        assert action.action_type == expected_action_type

    def test_missing_dict_key(self):
        assert Action.create({}).action_type == ActionType.NONE
