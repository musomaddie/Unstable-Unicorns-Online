from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.simulation.graphics.widget import Widget


class Controller(Widget):
    def __init__(self):
        super().__init__(QVBoxLayout())
