from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.gui.players.player_ui import PlayerWithUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label
from unstable_unicorns_game.gui.widgets.stacked_widget import StackedWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class PlayersOverviewRows:
    """ A variant of PlayersSpaceUi where the players are displayed in rows with all information visible."""
    player_to_uis: list[PlayerWithUi]
    view: ContainerWidget

    def __init__(self, to_uis: list[PlayerWithUi]):
        self.player_to_uis = to_uis
        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[wui.ui for wui in self.player_to_uis]
        )


class PlayersSpaceUi(StackedWidget):
    """ The space on the tabletop where all player boards are displayed.

    This is a stacked widget as the layout used depends on whose turn it is, and what view mode is selected.
    """

    overview_view: PlayersOverviewRows
    # TODO -> the current player views should be a list of tuples with players to uis (or similar) so it's easy to
    #  determine which corresponds to what player.
    current_player_view: Widget

    def __init__(self, all_players: AllPlayers, **kwargs):
        self.overview_view = PlayersOverviewRows(
            [PlayerWithUi(player, Label(player.name)) for player in all_players]
        )
        self.current_player_view = Label("first player view")
        super().__init__(
            children=[
                self.overview_view.view,
                self.current_player_view,
            ],
            **kwargs)

    def change_players_view(self):
        if self.layout.currentWidget() == self.overview_view.view.widget:
            self.change_view(self.current_player_view)
        else:
            self.change_view(self.overview_view.view)
