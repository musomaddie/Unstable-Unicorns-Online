""" area for cards to be displayed. """

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.hand_board import HandUi
from unstable_unicorns_game.simulation.graphics.player.stable_area import StableUi
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


class PlayerCardsUi:
    """ Contains all the cards the player has, including their hand and stable. """
    # TODO -> figure out somehow to make sure this all updates when the underlying data changes.
    hand: HandUi
    stable: StableUi

    expanded_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, player: Player):
        self.player = player
        self.hand = HandUi(player.hand)
        self.stable = StableUi(player.stable)

        self.expanded_view = ContainerWidget(QHBoxLayout())
        self.expanded_view.add_widgets(self.hand.expanded_view, self.stable.expanded_view)

        self.compact_view = ContainerWidget(QVBoxLayout())
        self.compact_view.add_widgets(self.hand.compact_view)

    def make_compact(self):
        # We just want to use the compact view instead. ... ?
        pass
