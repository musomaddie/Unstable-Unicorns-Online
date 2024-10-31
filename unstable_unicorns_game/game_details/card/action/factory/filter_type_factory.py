""" Factory for creating FilterType instances. """
from unstable_unicorns_game.game_details.card.action import FilterType


def create_default() -> FilterType:
    """ Creates a default filter. """
    return FilterType.NONE


def create(filter_str: str) -> FilterType:
    """ Creates a filter matching the given string. """
    for enum in FilterType:
        if enum.value == filter_str:
            return enum
    return create_default()
