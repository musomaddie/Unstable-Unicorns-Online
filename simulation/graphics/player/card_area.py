""" area for cards to be displayed. """
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from simulation.graphics.player.hand_board import HandBoard
from simulation.graphics.utility import Widget


class CardArea(Widget):
    """ Where all the players cards will live. """

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.style({"background-color": "#f5eac1;"})
        self.layout.addWidget(HandBoard.create_widget())

    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget
