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
        self.center = TableCenterUi(game)
        self.players_ui = PlayersUi(game.players)

        super().__init__(
            QVBoxLayout(), children=[self.center.view, self.players_ui.overview_widget])

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

    def change_current_player(self):
        self.players_ui.overview_widget.teardown()
        self.players_ui.current_player_widget.teardown()
        self.players_ui.current_player_widget.relayout()
        self.add_widgets(self.players_ui.current_player_widget)
        pass

    def update_user_choice_text(self, text: str):
        self.players_ui.current_player_ui().update_user_choice_text(text)

    def update_ui(self, deck: bool = False, discard_pile: bool = False, hand: bool = False, stable: bool = False):
        self.center.update(deck, discard_pile)
        self.players_ui.update_current_player_view(hand, stable)

    def enable_card_choice(self, on_click: Callable[[Card], None]):
        """ Allows the current player to choose a card to play. """
        self.players_ui.current_player_ui().enable_card_choice(on_click)

    def disable_card_choice(self):
        self.players_ui.current_player_ui().disable_card_choice()
