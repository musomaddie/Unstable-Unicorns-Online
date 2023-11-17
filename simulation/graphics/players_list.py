""" list of all players. """
from PyQt6.QtWidgets import QVBoxLayout, QWidget

from simulation.graphics.player import PlayerBoard
from simulation.graphics.utility import Widget


class PlayersList(Widget):
    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())

        for index, name in enumerate(["Aelin", "Brannon", "Chaol", "Dorian"]):
            self.layout.addWidget(
                PlayerBoard.create_widget(name, condensed=index != 0)
            )
