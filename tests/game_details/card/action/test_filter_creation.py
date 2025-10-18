import pytest

from unstable_unicorns_game.game_details.card.action.filter import Filter
from unstable_unicorns_game.game_details.card.action.filter_type import FilterType


class TestCreateDefault:
    def test_create_default_returns_empty_filters(self):
        result = Filter.create_default()
        assert len(result.filters) == 0


class TestCreate:
    @pytest.mark.parametrize(
        ("input_dict", "expected_filters"),
        [
            ({"filters": ["upgrade"]}, {FilterType.UPGRADE}),
            ({"filters": ["none"]}, {FilterType.NONE}),
            ({"filters": ["upgrade", "none"]}, {FilterType.UPGRADE, FilterType.NONE}),
            ({"filters": []}, set()),
        ]
    )
    def test_create_with_valid_filters(self, input_dict, expected_filters):
        result = Filter.create(input_dict)
        assert result.filters == expected_filters

    def test_create_missing_filters_key(self):
        result = Filter.create({})
        assert result.filters == set()

    def test_create_with_invalid_filter_string(self):
        result = Filter.create({"filters": ["invalid_filter"]})
        assert result.filters == {FilterType.NONE}

    def test_merges_identical_filters(self):
        result = Filter.create({"filters": ["none", "none"]})
        assert result.filters == {FilterType.NONE}

    def test_create_with_mixed_valid_invalid_filters(self):
        result = Filter.create({"filters": ["upgrade", "invalid", "none"]})
        assert result.filters == {FilterType.UPGRADE, FilterType.NONE}

    def test_create_with_empty_string_filter(self):
        result = Filter.create({"filters": [""]})
        assert result.filters == {FilterType.NONE}
