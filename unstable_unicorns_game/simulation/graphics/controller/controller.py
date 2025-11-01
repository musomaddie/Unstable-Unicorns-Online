from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.utility import Widget


class Controller(Widget):
    def __init__(self, game: Game):
        super().__init__(QVBoxLayout())
