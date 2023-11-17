""" area for cards to be displayed. """
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from simulation.graphics.player.hand_board import HandBoard
from simulation.graphics.player.stable_area import StableArea, Unicorns, GradesArea
from simulation.graphics.utility import Widget


class CardArea(Widget):
    """ Where all the players cards will live. """

    def __init__(self, condensed: bool):
        super().__init__(QHBoxLayout())
        self.style({"background-color": "#f5eac1;"})
        self.layout.addWidget(HandBoard.create_widget(condensed))

        if not condensed:
            self.layout.addWidget(StableArea.create_widget())
        else:
            stable = StableArea()
            self.layout.addWidget(stable.stable_lbl)
            self.layout.addWidget(Unicorns.create_widget())
            self.layout.addWidget(GradesArea.create_widget())

    @classmethod
    def create_widget(cls, condensed: bool) -> QWidget:
        return cls(condensed).widget
