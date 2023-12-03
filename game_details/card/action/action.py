""" action """
from dataclasses import dataclass

from game_details.card.action.action_type import ActionType
from game_details.card.action.filter import Filter


@dataclass
class Action:
    """ Class to manage card actions. """
    action_type: ActionType
    filter: Filter
