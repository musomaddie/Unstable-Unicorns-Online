""" Filter """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.action.filter_type import FilterType


@dataclass
class Filter:
    """ List of filters to be applied """
    filters: set[FilterType]

    @classmethod
    def create_default(cls) -> 'Filter':
        """ Creates a filter with an empty list."""
        return cls(filters=set())

    @classmethod
    def create(cls, action_dict: dict) -> 'Filter':
        """ Creates a filter object from the given dictionary. """
        if "filters" not in action_dict:
            return cls.create_default()

        return cls(filters=set([FilterType.create_from_string(f) for f in action_dict["filters"]]))
