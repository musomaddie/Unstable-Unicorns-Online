""" filter test. """
from game_details.card.action import FilterType
from game_details.card.action.factory import filter_factory


def test_create_default():
    assert filter_factory.create_default().filters == []


class TestCreate:

    def test_missing_dict_key(self):
        assert filter_factory.create({}).filters == []

    def test_one_item(self):
        result = filter_factory.create({"filters": ["upgrade"]})
        assert len(result.filters) == 1
        assert result.filters[0] == FilterType.UPGRADE

    def test_two_items(self):
        result = filter_factory.create({"filters": ["", "upgrade", "none"]})
        assert len(result.filters) == 3
        assert result.filters[0] == FilterType.NONE
        assert result.filters[1] == FilterType.UPGRADE
        assert result.filters[2] == FilterType.NONE
