""" Factory for creating Action instances. """
from game_details.card.action import Action, ActionType, Filter


def create_default() -> Action:
    """ Creates a default action. """
    return Action(action_type=ActionType.create_default(), filter=Filter.create_default())


def create(card_info) -> Action:
    """ Creates an action from the given dictionary. Passed the full card dict to handle if the key is missing. """
    if "action" in card_info:
        return Action(
            ActionType.create(card_info["action"]),
            Filter.create(card_info["action"]))
    return create_default()
