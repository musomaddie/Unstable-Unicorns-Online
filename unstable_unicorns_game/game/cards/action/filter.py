""" Filter """
from dataclasses import dataclass

from unstable_unicorns_game.game.cards.action.filter_type import FilterType


@dataclass
class Filter:
    """ List of filters to be applied """
    filters: list[FilterType]

    def __len__(self):
        return len(self.filters)

    def __iter__(self):
        yield from self.filters

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
