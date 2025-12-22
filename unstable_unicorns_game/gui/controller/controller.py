""" Manages interactions between the UI and the game. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.tabletop.table_top import TableTopUi
from unstable_unicorns_game.gui.widgets.button import Button
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class Controller:
    game: Game
    tabletop: TableTopUi
    view: ContainerWidget

    def __init__(self, game: Game, tabletop: TableTopUi):
        self.game = game
        self.tabletop = tabletop
        self.toggle_view_button = Button("Toggle View", self.toggle_players_view)

        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[
                self.toggle_view_button
            ],
            margins=Margins(right=20, left=20),
        )

    def toggle_players_view(self):
        self.tabletop.players_space.change_players_view()
