""" list of all players. """

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.all_players import AllPlayers
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


def create_current_player_widget(player_uids: list[PlayerUi]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    widget.add_widgets(*[ui.current_player_widget for ui in player_uids])
    return widget


class PlayersUi:
    """ Information about all of the players. """
    players: AllPlayers

    player_uis: list[PlayerUi]

    overview_widget: ContainerWidget
    current_player_widget: ContainerWidget

    def __init__(self, players: AllPlayers):
        self.players = players

        self.player_uis = [PlayerUi(player, color_code) for player, color_code in zip(players, color_list)]

        self.overview_widget = create_overview_widget(self.player_uis)
        self.current_player_widget = create_current_player_widget(self.player_uis)
        # TODO -> other widgets
