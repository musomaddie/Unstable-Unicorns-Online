""" area for cards to be displayed. """
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from unstable_unicorns_game.game_details.player import Player
from unstable_unicorns_game.simulation.graphics.player.hand_board import HandBoard
from unstable_unicorns_game.simulation.graphics.player.stable_area import StableArea
from unstable_unicorns_game.simulation.graphics.utility import Widget


class CardArea(Widget):
    """ Where all the players cards will live. """

    def __init__(self, player: Player):
        super().__init__(QHBoxLayout())
        self.layout.addWidget(HandBoard.create_widget(player.hand))
        self.layout.addWidget(StableArea.create_widget(player.stable))

    @classmethod
    def create_widget(cls, player: Player) -> QWidget:
        return cls(player).widget
