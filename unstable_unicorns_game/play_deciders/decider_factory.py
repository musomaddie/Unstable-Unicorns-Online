""" factory for creating the play decider. """
from unstable_unicorns_game.play_deciders.decider_type import DeciderType
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider


def create(decider_type_str: str, decisions: list[str] = ""):
    """ Factory for creating instances of PlayDecider. """
    if decider_type_str == "cli":
        return PlayDecider(DeciderType.CLI)
    if decider_type_str == "queue":
        return PlayDecider(DeciderType.QUEUE)

    if decider_type_str.startswith("test"):
        return PlayDecider(DeciderType.TEST, decisions)

    raise NotImplemented(f"{decider_type_str} does not corresponding to a recognised decider type.")
