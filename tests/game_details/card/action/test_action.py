from unstable_unicorns_game.game_details.card.action.action import Action
from unstable_unicorns_game.game_details.card.action.action_type import ActionType
from unstable_unicorns_game.game_details.card.action.filter_type import FilterType


class TestCreateDefault:
    def test_create_default_returns_none_action_and_empty_filter(self):
        result = Action.create_default()
        assert result.action_type == ActionType.NONE
        assert result.filter.filters == set()


class TestCreate:
    def test_create_with_action_type_only(self):
        card_info = {"action": {"action_type": "steal"}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == set()

    def test_create_with_action_type_and_filters(self):
        card_info = {"action": {"action_type": "steal", "filters": ["upgrade"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == {FilterType.UPGRADE}

    def test_create_with_action_type_and_multiple_filters(self):
        card_info = {"action": {"action_type": "steal", "filters": ["upgrade", "none"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == {FilterType.UPGRADE, FilterType.NONE}

    def test_create_missing_action_key(self):
        card_info = {}
        result = Action.create(card_info)
        assert result.action_type == ActionType.NONE
        assert result.filter.filters == set()

    def test_create_missing_action_type_key(self):
        card_info = {"action": {"filters": ["upgrade"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.NONE
        assert result.filter.filters == {FilterType.UPGRADE}

    def test_create_with_invalid_action_type(self):
        card_info = {"action": {"action_type": "invalid_action"}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.NONE
        assert result.filter.filters == set()

    def test_create_with_invalid_filters(self):
        card_info = {"action": {"action_type": "steal", "filters": ["invalid_filter"]}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == {FilterType.NONE}

    def test_create_with_empty_action_dict(self):
        card_info = {"action": {}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.NONE
        assert result.filter.filters == set()

    def test_create_with_empty_filters_list(self):
        card_info = {"action": {"action_type": "steal", "filters": []}}
        result = Action.create(card_info)
        assert result.action_type == ActionType.STEAL
        assert result.filter.filters == set()
