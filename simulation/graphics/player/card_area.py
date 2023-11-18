""" area for cards to be displayed. """
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from game_details.player import Player
from simulation.graphics.player.hand_board import HandBoard
from simulation.graphics.player.stable_area import StableArea
from simulation.graphics.utility import Widget


class CardArea(Widget):
    """ Where all the players cards will live. """

    def __init__(self, player: Player):
        super().__init__(QHBoxLayout())
        self.style({"background-color": "#f5eac1;"})
        self.layout.addWidget(HandBoard.create_widget(player.hand))

        self.layout.addWidget(StableArea.create_widget(player.stable))

    @classmethod
    def create_widget(cls, player: Player) -> QWidget:
        return cls(player).widget
