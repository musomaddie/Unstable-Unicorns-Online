""" list of all players. """

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_ui import PlayerUi
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


def create_current_player_view(
        players: AllPlayers,
        to_uis: list[tuple[Player, PlayerUi]]) -> ContainerWidget:
    # The current player gets a special view, all the others go in a row down the bottom (including the current
    # player, but theirs is just an initial).

    current_player = [
        player_ui.current_player_view for player, player_ui in to_uis if player == players.current_player()][0]

    row_widget = ContainerWidget(
        QHBoxLayout(), remove_margins=True,
        children=[player_ui.summary_view for _, player_ui in to_uis])

    view_widget = ContainerWidget(
        QVBoxLayout(), vertical_stretch=1, margins=Margins(top=0),
        children=[current_player, row_widget])

    return view_widget


class PlayersUi:
    """ Information about all of the players. """
    players: AllPlayers

    players_to_uis = list[tuple[Player, PlayerUi]]

    overview_widget: ContainerWidget
    current_player_widget: ContainerWidget

    def __init__(self, players: AllPlayers):
        self.players = players

        self.players_to_uis = [
            (player, PlayerUi(player, color_code)) for player, color_code in zip(players, color_list)
        ]
        self.overview_widget = create_overview_widget([ui for _, ui in self.players_to_uis])
        self.current_player_widget = create_current_player_view(self.players, self.players_to_uis)

    def current_player_ui(self) -> PlayerUi:
        return [
            ui for player, ui in self.players_to_uis if player == self.players.current_player()
        ][0]

    def update_current_player_hand_view(self):
        self.current_player_ui().update_hand_view()
