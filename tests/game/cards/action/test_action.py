from pytest_unordered import unordered

from unstable_unicorns_game.game.cards.action.action import Action
from unstable_unicorns_game.game.cards.action.action_type import ActionType
from unstable_unicorns_game.game.cards.action.filter_type import FilterType


class TestCreateDefault:
    def test_create_default_returns_none_action_and_empty_filter(self):
        result = Action.create_default()
        assert result.action_type == ActionType.NONE
        assert len(result.filter) == 0


class TestCreate:
    def test_create_with_action_type_only(self):
        card_info = {"action": {"action_type": "steal"}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert len(result.filter) == 0

    def test_create_with_action_type_and_filters(self):
        card_info = {"action": {"action_type": "steal", "filters": ["upgrade"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == [FilterType.UPGRADE]

    def test_create_with_action_type_and_multiple_filters(self):
        card_info = {"action": {"action_type": "steal", "filters": ["upgrade", "none"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == unordered([FilterType.UPGRADE, FilterType.NONE])
