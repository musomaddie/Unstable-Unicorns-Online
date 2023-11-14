""" Filter """
from dataclasses import dataclass

from game_details.card.action.filter_type import FilterType


@dataclass
class Filter:
    """ List of filters to be applied """
    filters: list[FilterType]

    @staticmethod
    def create_default() -> 'Filter':
        """ Creates a filter with an empty list."""
        return Filter(filters=[])

    @staticmethod
    def create(action_dict: dict) -> 'Filter':
        """ Creates a filter object from the given dictionary. """
        if "filters" not in action_dict:
            return Filter.create_default()

        return Filter(filters=[FilterType.create(f) for f in action_dict["filters"]])
