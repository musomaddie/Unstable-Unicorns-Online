""" test for action """
import pytest

from game_details.card.action import Action, ActionType, FilterType


def test_create_default():
    action = Action.create_default()
    assert action.action_type == ActionType.NONE
    assert len(action.filter.filters) == 0


class TestCreate:

    @pytest.mark.parametrize(
        ("action_type_str", "expected_action_type"),
        [("steal", ActionType.STEAL), ("none", ActionType.NONE)])
    def test_with_dict_action_type(self, action_type_str, expected_action_type):
        action = Action.create({"action": {"action_type": action_type_str}})
        assert action.action_type == expected_action_type
        assert action.filter.filters == []

    @pytest.mark.parametrize(
        ("filter_string", "expected_filter_list"),
        [([], []), (["upgrade"], [FilterType.UPGRADE]), (["upgrade", "none"], [FilterType.UPGRADE, FilterType.NONE])]
    )
    def test_with_dict_filter(self, filter_string, expected_filter_list):
        action = Action.create({"action": {"filters": filter_string}})
        assert action.action_type == ActionType.NONE
        assert action.filter.filters == expected_filter_list

    def test_with_dict_all(self):
        action = Action.create({
            "action": {
                "action_type": "steal",
                "filters": ["upgrade"]}
        })
        assert action.action_type == ActionType.STEAL
        assert action.filter.filters == [FilterType.UPGRADE]

    def test_missing_dict_key(self):
        assert Action.create({}).action_type == ActionType.NONE
