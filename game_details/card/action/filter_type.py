""" Filter type """
from enum import Enum


class FilterType(Enum):
    """ Filter type. """
    UPGRADE = "upgrade"
    NONE = "none"

    @staticmethod
    def create_default() -> 'FilterType':
        """ Creates a default filter. """
        return FilterType.NONE

    @staticmethod
    def create(filter_str: str) -> 'FilterType':
        """ Creates a filter matching the given string. """
        for enum in FilterType:
            if enum.value == filter_str:
                return enum
        return FilterType.create_default()
