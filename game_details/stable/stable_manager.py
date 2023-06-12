from game_details.stable.stable import Stable


class StableManager:
    """ Manages interactions with a players stable."""

    def __init__(self, stable: Stable):
        self.stable = stable
