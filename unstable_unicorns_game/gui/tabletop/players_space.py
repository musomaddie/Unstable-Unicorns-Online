from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player
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


class SummarySpot(StackedWidget):
    summary_view: ContainerWidget
    placeholder_view: ContainerWidget

    def __init__(self, player_ui: PlayerUi):
        self.summary_view = player_ui.summary_view
        self.placeholder_view = player_ui.placeholder_view

        super().__init__(children=[self.summary_view, self.placeholder_view])

    def use_placeholder(self):
        self.change_view(self.placeholder_view)

    def use_summary(self):
        self.change_view(self.summary_view)


class CurrentPlayerSpace(StackedWidget):
    """ Represents the space on the tabletop where information relating to the CURRENT player is displayed. """

    player_uis: list[PlayerUi]
    player: PlayerUi

    def __init__(self, player_uis: list[PlayerUi], **kwargs):
        self.player_uis = player_uis
        # Default to the first player as the current player.
        self.player = player_uis[0]
        super().__init__(
            children=[ui.detailed_view.view for ui in self.player_uis],
            **kwargs)

    def change_player(self, new_player: Player):
        print("should be changing player.")
        pass


class PlayersTurnView:
    """ A variant of PlayersSpaceUi where the players summaries are displayed beneath the current players turn view.
    """
    players: AllPlayers
    player_uis: list[PlayerUi]
    current_player_space: CurrentPlayerSpace
    view: ContainerWidget

    def __init__(self, to_uis: list[PlayerUi], players: AllPlayers):
        self.players = players
        self.player_uis = to_uis

        self.current_player_space = CurrentPlayerSpace(self.player_uis)

        # Default to using the first player as the current player upon creation.
        summary_spots = [SummarySpot(ui) for ui in self.player_uis]
        summary_spots[0].use_placeholder()

        summary_views = ContainerWidget(
            QHBoxLayout(),
            children=summary_spots,
        )

        self.view = ContainerWidget(
            QVBoxLayout(),
            children=[
                # TODO -> store the current player views in a way that allows us to control which one is shown here.
                #  Should be just shoving them into a stacked widget.
                # Current player view
                self.current_player_space,
                summary_views
            ],
        )

    def change_player(self, new_current_player: Player):
        self.current_player_space.change_player(new_current_player)

    def update_choice_text(self, text: str):
        # TODO -> update to reference the current player, not just the first one. (and same for the following methods)
        self.current_player_space.player.detailed_view.update_choice_text(text)

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        self.current_player_space.player.cards_space.enable_card_selection(on_click)

    def disable_card_selection(self):
        self.current_player_space.player.cards_space.disable_card_selection()


class PlayersSpaceUi(StackedWidget):
    """ The space on the tabletop where all player boards are displayed.

    This is a stacked widget as the layout used depends on whose turn it is, and what view mode is selected.
    """
    uis: list[PlayerUi]

    overview_view: PlayersOverviewRows
    current_player_view: PlayersTurnView

    def __init__(self, all_players: AllPlayers, **kwargs):
        self.uis = [PlayerUi(player, color_code) for player, color_code in zip(all_players, players_color_list)]
        self.overview_view = PlayersOverviewRows(self.uis)
        self.current_player_view = PlayersTurnView(self.uis, all_players)
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

    def update(self, hand: bool = False, stable: bool = False):
        for ui in self.uis:
            ui.update(hand, stable)

    def change_current_player(self, player: Player):
        self.current_player_view.change_player(player)
