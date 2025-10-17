""" Factory for creating Action instances. """
from unstable_unicorns_game.game_details.card.action.action import Action
# from
from unstable_unicorns_game.game_details.card.action.action_type import ActionType
from unstable_unicorns_game.game_details.card.action.factory import filter_factory


def create_default() -> Action:
    """ Creates a default action. """
    return Action(ActionType.create_default(), filter=filter_factory.create_default())


def create(card_info) -> Action:
    """ Creates an action from the given dictionary. Passed the full card dict to handle if the key is missing. """
    if "action" in card_info:
        return Action(
            ActionType.create_from_dict(card_info["action"]),
            filter_factory.create(card_info["action"]))
    return create_default()
