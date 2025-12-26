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

        self.view = ContainerWidget(QHBoxLayout(), children=[self.hand.view, self.stable.view])
        self.compact_view = ContainerWidget(QVBoxLayout(), children=[self.hand.compact_view])
