""" Factory for creating action_type instances. """
from game_details.card.action import ActionType


def create_default() -> ActionType:
    """ Creates a default action type. """
    return ActionType.NONE


def create(action_dict: dict) -> 'ActionType':
    """ Creates an action type given the dictionary. """
    if "action_type" not in action_dict:
        return create_default()
    desc = action_dict["action_type"]
    for enum in ActionType:
        if enum.value == desc:
            return enum
    return create_default()
