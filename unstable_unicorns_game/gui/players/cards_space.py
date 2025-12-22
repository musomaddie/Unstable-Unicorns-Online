from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.gui.players.hand_ui import HandUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label
from unstable_unicorns_game.gui.widgets.widget import Widget


class PlayerCardsSpace:
    """ Space for cards belonging to this player. """
    hand: HandUi
    stable: Widget

    view: ContainerWidget

    def __init__(self, player: Player):
        self.hand = HandUi(player.hand)
        self.stable = Label("Stable")

        self.view = ContainerWidget(
            QHBoxLayout(), children=[self.hand.view.overall_view, self.stable]
        )
