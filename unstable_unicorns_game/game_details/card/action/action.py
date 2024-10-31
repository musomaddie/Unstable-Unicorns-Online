""" action """
from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.action.action_type import ActionType
from unstable_unicorns_game.game_details.card.action.filter import Filter


@dataclass
class Action:
    """ Class to manage card actions. """
    action_type: ActionType
    filter: Filter
