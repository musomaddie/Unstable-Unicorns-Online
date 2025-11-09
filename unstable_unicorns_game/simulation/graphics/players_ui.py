""" list of all players. """

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.simulation.graphics.player.player_ui import PlayerUi
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget

color_list = [
    "#DEDAF4",
    "#D9EDF8",
    "#E4F1EE",
    "#FDFFB6",
    "#FFD6A5",
    "#FFADAD",
]


def create_overview_widget(player_uis: list[PlayerUi]) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout())
    widget.add_widgets(*[ui.overview_widget for ui in player_uis])
    return widget


def create_current_player_view(
        players: AllPlayers,
        to_uis: list[tuple[Player, PlayerUi]]) -> ContainerWidget:
    # The current player gets a special view, all the others go in a row down the bottom (including the current
    # player, but theirs is just an initial).

    row_widget = ContainerWidget(QHBoxLayout())
    view_widget = ContainerWidget(QVBoxLayout())

    row_widget.add_widgets(*[player_ui.current_player_widget for player, player_ui in to_uis])
    row_widget.remove_margins()

    # For now keep it simple - just reuse all the existing widgets, can make the special ones later.
    for player, player_ui in to_uis:
        if player == players.current_player():
            view_widget.add_widgets(player_ui.overview_widget)

    view_widget.add_widgets(row_widget)

    return view_widget


class PlayersUi:
    """ Information about all of the players. """
    players: AllPlayers

    players_to_uis = list[tuple[Player, PlayerUi]]

    player_uis: list[PlayerUi]

    overview_widget: ContainerWidget
    current_player_widget: ContainerWidget

    def __init__(self, players: AllPlayers):
        self.players = players

        self.players_to_uis = [
            (player, PlayerUi(player, color_code)) for player, color_code in zip(players, color_list)
        ]
        self.player_uis = [PlayerUi(player, color_code) for player, color_code in zip(players, color_list)]

        self.overview_widget = create_overview_widget(self.player_uis)
        self.current_player_widget = create_current_player_view(self.players, self.players_to_uis)
        # TODO -> other widgets
