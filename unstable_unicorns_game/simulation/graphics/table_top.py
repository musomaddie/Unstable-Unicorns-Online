""" table top (center layout)"""
from typing import Callable

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.players_ui import PlayersUi
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenterUi
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget

"""
How should the view mode info be structured?? 

TABLE
    -> OVERVIEW 
    -> CURRENT PLAYER ,
    
each of these include how the player boards should look, which in turn declare how x y z should look. 

# class PlayerViewMode(Enum):
#     OVERVIEW = auto()
#     CURRENT_PLAYER = auto()
#     SUMMARISED = auto()


Will come back to this a bit later.

"""


class TableTop(ContainerWidget):
    center: TableCenterUi
    players_ui: PlayersUi
    game: Game

    def __init__(self, game: Game):
        self.game = game
        super().__init__(QVBoxLayout())

        self.center = TableCenterUi(game)
        self.players_ui = PlayersUi(game.players)
        self.add_widgets(self.center.view, self.players_ui.overview_widget)

    def make_compact(self):
        self.players_ui.overview_widget.teardown()
        self.players_ui.current_player_widget.relayout()
        # TODO -> Because the center hasn't been readded, the tabletop widget no longer includes it within its children.
        self.add_widgets(self.players_ui.current_player_widget)

    def make_expanded(self):
        self.players_ui.current_player_widget.teardown()
        self.players_ui.overview_widget.relayout()
        # TODO -> Because the center hasn't been readded, the tabletop widget no longer includes it within its children.
        self.add_widgets(self.players_ui.overview_widget)

    def update_ui_after_draw(self):
        self.center.update_after_draw()
        self.players_ui.update_current_player_hand_view()

    def prepare_choose_card_to_play(self, game_runnable: Callable[[Card], None]):
        """ Allows the current player to choose a card to play. """
        print("I am setting up onclick")
        self.players_ui.current_player_ui().prepare_choose_card_to_play(game_runnable)

    def cleanup_choose_card_to_play(self):
        self.players_ui.current_player_ui().cleanup_choose_card_to_play()
