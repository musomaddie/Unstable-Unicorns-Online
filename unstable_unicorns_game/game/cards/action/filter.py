""" Filter """
from dataclasses import dataclass

from unstable_unicorns_game.game.cards.action.filter_type import FilterType


@dataclass
class Filter:
    """ List of filters to be applied """
    filters: list[FilterType]

    def __len__(self):
        return len(self.filters)

    def __iter__(self) -> '_FilterIterator':
        return _FilterIterator(self)

    @classmethod
    def create_default(cls) -> 'Filter':
        """ Creates a filter with an empty list."""
        return cls(filters=[])

    @classmethod
    def create(cls, action_dict: dict) -> 'Filter':
        """ Creates a filter object from the given dictionary. """
        if "filters" not in action_dict:
            return cls.create_default()
        return cls(list(set([FilterType.create_from_string(f) for f in action_dict["filters"]])))


class _FilterIterator:
    """ An iterator for the filter"""

    def __init__(self, filter: Filter):
        self._filter = filter
        self._index = 0

    def __next__(self) -> FilterType:
        if self._index < len(self._filter):
            self._index += 1
            return self._filter.filters[self._index - 1]
        raise StopIteration
