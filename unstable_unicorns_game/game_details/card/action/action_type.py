""" action type"""
from enum import Enum


class ActionType(Enum):
    """ The type of action. """
    STEAL = "steal"
    NONE = "none"

    @classmethod
    def create_default(cls) -> 'ActionType':
        return cls.NONE

    @classmethod
    def create_from_dict(cls, action_dict: dict) -> 'ActionType':
        if "action_type" not in action_dict:
            return cls.create_default()

        desc = action_dict["action_type"]
        for enum in cls:
            if enum.value == desc:
                return enum
        return cls.create_default()
