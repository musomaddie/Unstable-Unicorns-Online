""" area for cards to be displayed. """

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.cards.cards import CardViewMode
from unstable_unicorns_game.simulation.graphics.player.hand_board import HandBoard
from unstable_unicorns_game.simulation.graphics.player.stable_area import StableArea
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


class CardArea(ContainerWidget):
    """ Where all the player's cards will live. """

    def __init__(self, player: Player):
        super().__init__(QHBoxLayout())
        self.view_mode = CardViewMode.EXPANDED

        self.hand_board = HandBoard(player.hand)
        self.stable_area = StableArea(player.stable)

        self.add_widgets(self.hand_board, self.stable_area)

    def _make_compact(self):
        self.hand_board.update_view_mode(CardViewMode.COMPACT)

    def update_view_mode(self, view_mode: CardViewMode):
        # Exit early if we're already in the desired mode.
        if view_mode == self.view_mode:
            return

        self.view_mode = view_mode
        if view_mode == CardViewMode.COMPACT:
            self._make_compact()

        # TODO -> implement other variants.
