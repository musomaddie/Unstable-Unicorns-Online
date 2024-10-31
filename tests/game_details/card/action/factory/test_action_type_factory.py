""" tests for action type """
import pytest

from unstable_unicorns_game.game_details.card.action import ActionType
from unstable_unicorns_game.game_details.card.action.factory import action_type_factory


class TestCreate:

    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [("steal", ActionType.STEAL), ("none", ActionType.NONE)])
    def test_create_corresponding_string(self, input_string, expected_result):
        action_type = action_type_factory.create({"action_type": input_string})
        assert action_type == expected_result

    def test_create_missing_dict_key(self):
        assert action_type_factory.create({}) == ActionType.NONE

    def test_create_spam(self):
        assert action_type_factory.create({"action_type": "adfjkdl;afj"}) == ActionType.NONE
