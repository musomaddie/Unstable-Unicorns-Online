from enum import Enum, auto
from typing import Callable

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.table_center.table_center import TableCenterUi
from unstable_unicorns_game.gui.tabletop.players_space import PlayersSpaceUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class ViewMode(Enum):
    OVERVIEW = auto()
    CURRENT_PLAYER = auto()


class TableTopUi:
    """
    Contains the entire game board (but not the controller). This includes the deck, discard pile, nursery, and players.
    """
    table_center: TableCenterUi

    players_space: PlayersSpaceUi
    view: ContainerWidget

    view_mode: ViewMode

    def __init__(self, game: Game):
        self.table_center = TableCenterUi(game)
        self.players_space = PlayersSpaceUi(game.players)
        self.view_mode = ViewMode.OVERVIEW
        self.view = ContainerWidget(
            QVBoxLayout(), children=[
                self.table_center.view,
                self.players_space,
            ])

    def update_view(self, view_mode: ViewMode):
        if view_mode == self.view_mode:
            return

        match view_mode:
            case ViewMode.OVERVIEW:
                self.players_space.use_overview_view()
            case ViewMode.CURRENT_PLAYER:
                self.players_space.use_players_view()

        self.view_mode = view_mode

    def update_players_choice_text(self, text: str):
        self.players_space.current_player_view.update_choice_text(text)

    def update_ui(self, deck: bool = False, hand: bool = False, stable: bool = False):
        if deck:
            self.table_center.deck.update()
        self.players_space.update(hand, stable)

    def enable_card_choice(self, on_click: Callable[[Card], None]):
        self.players_space.current_player_view.enable_card_selection(on_click)

    def disable_card_choice(self):
        self.players_space.current_player_view.disable_card_selection()
