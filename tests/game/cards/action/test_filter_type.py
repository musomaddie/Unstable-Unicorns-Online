import pytest

from unstable_unicorns_game.game.cards.action.filter_type import FilterType


class TestCreateDefault:
    def test_create_default_returns_none(self):
        assert FilterType.create_default() == FilterType.NONE


class TestCreateFromString:
    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [
            ("upgrade", FilterType.UPGRADE),
            ("none", FilterType.NONE),
        ]
    )
    def test_create_corresponding_type(self, input_string, expected_result):
        assert FilterType.create_from_string(input_string) == expected_result

    def test_create_invalid_string(self):
        assert FilterType.create_from_string("invalid_filter") == FilterType.NONE

    def test_create_empty_string(self):
        assert FilterType.create_from_string("") == FilterType.NONE
