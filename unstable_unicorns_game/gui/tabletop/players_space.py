from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.gui.players.player_ui import PlayerUi
from unstable_unicorns_game.gui.resources.color import players_color_list
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.stacked_widget import StackedWidget


class PlayersOverviewRows:
    """ A variant of PlayersSpaceUi where the players are displayed in rows with all information visible."""
    player_uis: list[PlayerUi]
    view: ContainerWidget

    def __init__(self, to_uis: list[PlayerUi]):
        self.player_uis = to_uis
        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[ui.overview_view for ui in self.player_uis],
        )


class PlayersTurnView:
    """ A variant of PlayersSpaceUi where the players summaries are displayed beneath the current players turn view.
    """
    players: AllPlayers
    player_uis: list[PlayerUi]
    view: ContainerWidget

    def __init__(self, to_uis: list[PlayerUi], players: AllPlayers):
        self.players = players
        self.player_uis = to_uis

        summary_views = ContainerWidget(
            QHBoxLayout(),
            children=[ui.summary_view for ui in self.player_uis],
        )
        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[
                # TODO -> store the current player views in a way that allows us to control which one is shown here.
                #  Should be just shoving them into a stacked widget.
                # Current player view
                self.player_uis[0].detailed_view.view,
                summary_views
            ],
            # TODO -> stretch! (the 2/3 current player, 1/3 summary
        )


class PlayersSpaceUi(StackedWidget):
    """ The space on the tabletop where all player boards are displayed.

    This is a stacked widget as the layout used depends on whose turn it is, and what view mode is selected.
    """

    overview_view: PlayersOverviewRows
    # TODO -> the current player views should be a list of tuples with players to uis (or similar) so it's easy to
    #  determine which corresponds to what player.
    current_player_view: PlayersTurnView

    def __init__(self, all_players: AllPlayers, **kwargs):
        uis = [PlayerUi(player, color_code) for player, color_code in zip(all_players, players_color_list)]
        self.overview_view = PlayersOverviewRows(uis)
        self.current_player_view = PlayersTurnView(uis, all_players)
        super().__init__(
            children=[
                self.overview_view.view,
                self.current_player_view.view,
            ],
            **kwargs)

    def use_overview_view(self):
        self.change_view(self.overview_view.view)

    def use_players_view(self):
        self.change_view(self.current_player_view.view)
