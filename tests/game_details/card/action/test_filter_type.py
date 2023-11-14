""" filter type test """
import pytest

from game_details.card.action import FilterType


def test_create_default():
    assert FilterType.create_default() == FilterType.NONE


class TestCreate:

    @pytest.mark.parametrize(
        ("input_string", "expected_result"),
        [("upgrade", FilterType.UPGRADE), ("none", FilterType.NONE)]
    )
    def test_corresponding_str(self, input_string, expected_result):
        assert FilterType.create(input_string) == expected_result

    def test_empty_str(self):
        assert FilterType.create("") == FilterType.NONE
