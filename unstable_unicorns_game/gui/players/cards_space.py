from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.gui.players.hand_ui import HandUi
from unstable_unicorns_game.gui.players.stable_ui import StableUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class PlayerCardsSpace:
    """ Space for cards belonging to this player. """
    hand: HandUi
    stable: StableUi

    view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, player: Player):
        self.hand = HandUi(player.hand)
        self.stable = StableUi(player.stable)

        # TODO -> it would be lovely if the horizontal stretch (included nested) was dynamic and responded to the number
        # of cards (even just roughly) in each section.
        self.view = ContainerWidget(QHBoxLayout(), children=[self.hand.view, self.stable.view], horizontal_stretch=5)
        self.compact_view = ContainerWidget(
            QVBoxLayout(),
            children=[self.hand.compact_view, self.stable.compact_view],
            vertical_stretch=2)
