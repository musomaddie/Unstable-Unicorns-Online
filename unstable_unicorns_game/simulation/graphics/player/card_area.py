""" area for cards to be displayed. """

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.cards.cards import CardViewMode
from unstable_unicorns_game.simulation.graphics.player.hand_board import HandBoard
from unstable_unicorns_game.simulation.graphics.player.stable_area import StableArea
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


# class ExpandedCarArea(ContainerWidget):
#     """ Information about the current cards the player has, both in their hand and their stable, shown in an extended form. """
#
#     def __init__(self, player: Player):
#         super().__init__(QHBoxLayout())
#         hand_board = HandBoard(player.hand)
#         stable_area = StableArea(player.stable)
#
#         self.add_widgets(hand_board, stable_area)
#
#
# class CompactCardArea(ContainerWidget):
#     """ A compact card a"""

class CardArea:
    """ Contains all the cards the player has, including their hand and stable. """

    def __init__(self, player: Player):
        self.player = player

        self.expanded_view = ContainerWidget(QHBoxLayout())
        self.expanded_view.add_widgets(HandBoard(player.hand), StableArea(player.stable))


# TODO -> how should I attach this?? should be enough for its caller to just call one.

class CardArea1(ContainerWidget):
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
