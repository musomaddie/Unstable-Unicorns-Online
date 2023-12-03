""" Factory for creating Filter instances. """
from game_details.card.action import Filter, FilterType


def create_default() -> Filter:
    """ Creates a filter with an empty list."""
    return Filter(filters=[])


def create(action_dict: dict) -> Filter:
    """ Creates a filter object from the given dictionary. """
    if "filters" not in action_dict:
        return create_default()

    return Filter(filters=[FilterType.create(f) for f in action_dict["filters"]])
