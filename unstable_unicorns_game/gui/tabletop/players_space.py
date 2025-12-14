from PyQt6.QtWidgets import QLabel

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.stacked_widget import StackedWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class PlayersSpaceUi(StackedWidget):
    """ The space on the tabletop where all player boards are displayed.

    This is a stacked widget as the layout used depends on whose turn it is. """

    overview_view: ContainerWidget
    # TODO -> the current player views should be a list of tuples with players to uis (or similar) so it's easy to
    #  determine which corresponds to what player.
    current_player_view: ContainerWidget

    def __init__(self, all_players: AllPlayers, **kwargs):
        super().__init__(
            children=[
                Widget(QLabel("All players!")),
                Widget(QLabel("First player view")),
            ],
            **kwargs)
