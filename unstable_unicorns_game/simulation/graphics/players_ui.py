""" list of all players. """

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_ui import CurrentPlayerWidget, PlayerSummaryView, PlayerUi
from unstable_unicorns_game.simulation.graphics.utility.measurements import Margins
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget

color_list = [
    "#DEDAF4",
    "#D9EDF8",
    "#E4F1EE",
    "#FDFFB6",
    "#FFD6A5",
    "#FFADAD",
]


def create_overview_widget(player_uis: list[PlayerUi]) -> ContainerWidget:
    return ContainerWidget(
        QVBoxLayout(), vertical_stretch=4, margins=Margins(top=0),
        children=[ui.overview_view for ui in player_uis])


class SummaryRowView:
    player_to_uis: list[tuple[Player, PlayerSummaryView]]
    widget: ContainerWidget

    def __init__(self, players: AllPlayers, to_uis: list[tuple[Player, PlayerUi]]):
        self.player_to_uis = [(player, ui.summary_view) for player, ui in to_uis]
        self.widget = ContainerWidget(
            QHBoxLayout(),
            remove_margins=True,
            children=[
                ui.initial_only_view if player == players.current_player() else ui.detail_view for player, ui in
                self.player_to_uis
            ]
        )


class CurrentPlayerFocusView:
    current_player_ui: CurrentPlayerWidget
    summary_row_ui: SummaryRowView
    widget: ContainerWidget

    # TODO -> surely it would be better to have the layouts functioning more like static data holders. so instead of
    # having a "current player view" that's intrinsically tied to a particular player, we have a current player
    # "template" that we populate with the relevant data.

    def __init__(self, players: AllPlayers, to_uis: list[tuple[Player, PlayerUi]]):
        self.current_player_ui = [
            player_ui.current_player_view for player, player_ui in to_uis if player == players.current_player()][0]
        self.summary_row_ui = SummaryRowView(players, to_uis)
        self.widget = ContainerWidget(
            QVBoxLayout(), vertical_stretch=1, margins=Margins(top=0),
            children=[self.current_player_ui, self.summary_row_ui.widget])

    def relayout(self):
        self.widget.relayout()

    def teardown(self):
        self.widget.teardown()


class PlayersUi:
    """ Information about all of the players. """
    players: AllPlayers

    players_to_uis = list[tuple[Player, PlayerUi]]

    overview_widget: ContainerWidget
    current_player_focus_view: CurrentPlayerFocusView

    def __init__(self, players: AllPlayers):
        self.players = players

        self.players_to_uis = [
            (player, PlayerUi(player, color_code)) for player, color_code in zip(players, color_list)
        ]
        self.overview_widget = create_overview_widget([ui for _, ui in self.players_to_uis])
        self.current_player_focus_view = CurrentPlayerFocusView(self.players, self.players_to_uis)

    def current_player_ui(self) -> PlayerUi:
        return [
            ui for player, ui in self.players_to_uis if player == self.players.current_player()
        ][0]

    def update_current_player_view(self, hand: bool = False, stable: bool = False):
        self.current_player_ui().update_view(hand, stable)
