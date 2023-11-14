""" action type"""
from enum import Enum


class ActionType(Enum):
    """ The type of action. """
    STEAL = "steal"
    NONE = "none"

    @staticmethod
    def create_default() -> 'ActionType':
        """ Creates a default action type. """
        return ActionType.NONE

    @staticmethod
    def create(action_dict: dict) -> 'ActionType':
        """ Creates an action type given the dictionary. """
        if "action_type" not in action_dict:
            return ActionType.create_default()
        desc = action_dict["action_type"]
        for enum in ActionType:
            if enum.value == desc:
                return enum
        return ActionType.create_default()
