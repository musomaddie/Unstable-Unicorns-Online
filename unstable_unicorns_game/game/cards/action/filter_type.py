""" Filter type """
from enum import Enum


class FilterType(Enum):
    """ Filter type. """
    UPGRADE = "upgrade"
    NONE = "none"

    @classmethod
    def create_default(cls) -> 'FilterType':
        return cls.NONE

    @classmethod
    def create_from_string(cls, filter_str: str) -> 'FilterType':
        for enum in cls:
            if enum.value == filter_str:
                return enum
        return cls.create_default()
