""" area for cards to be displayed. """
from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.hand_board import HandBoard
from unstable_unicorns_game.simulation.graphics.player.stable_area import StableArea
from unstable_unicorns_game.simulation.graphics.widget import Widget


class CardArea(Widget):
    """ Where all the players cards will live. """

    def __init__(self, player: Player):
        super().__init__(QHBoxLayout())
        self.layout.addWidget(HandBoard(player.hand).widget)
        self.layout.addWidget(StableArea(player.stable).widget)
