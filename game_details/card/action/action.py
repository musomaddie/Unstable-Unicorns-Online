""" action """
from dataclasses import dataclass

from game_details.card.action.action_type import ActionType
from game_details.card.action.filter import Filter


@dataclass
class Action:
    """ Class to manage card actions. """
    action_type: ActionType
    filter: Filter

    @staticmethod
    def create_default() -> 'Action':
        """ Creates a default action. """
        return Action(action_type=ActionType.create_default(), filter=Filter.create_default())

    @staticmethod
    def create(card_info) -> 'Action':
        """ Creates an action from the given dictionary. Passed the full card dict to handle if the key is missing. """
        if "action" in card_info:
            return Action(
                ActionType.create(card_info["action"]),
                Filter.create(card_info["action"]))
        return Action.create_default()
