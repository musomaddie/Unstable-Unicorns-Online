""" action """
from dataclasses import dataclass

from unstable_unicorns_game.game.card.action.action_type import ActionType
from unstable_unicorns_game.game.card.action.filter import Filter


@dataclass
class Action:
    """ Class to manage card actions. """
    action_type: ActionType
    filter: Filter

    @classmethod
    def create_default(cls) -> 'Action':
        """ Creates a default action. """
        return cls(ActionType.create_default(), filter=Filter.create_default())

    @classmethod
    def create(cls, card_info: dict) -> 'Action':
        """ Creates an action from the given dictionary. Passed the full card dict to handle if the key is missing. """
        if "action" in card_info:
            return cls(
                ActionType.create_from_dict(card_info["action"]),
                Filter.create(card_info["action"]))
        return cls.create_default()
