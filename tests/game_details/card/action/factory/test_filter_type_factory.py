""" filter type test """
import pytest

from game_details.card.action import FilterType
from game_details.card.action.factory import filter_type_factory


def test_create_default():
    assert filter_type_factory.create_default() == FilterType.NONE


class TestCreate:

    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [("upgrade", FilterType.UPGRADE), ("none", FilterType.NONE)]
    )
    def test_corresponding_str(self, input_string, expected_result):
        assert filter_type_factory.create(input_string) == expected_result

    def test_empty_str(self):
        assert filter_type_factory.create("") == FilterType.NONE
