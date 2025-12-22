from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.gui.widgets.label import Label
from unstable_unicorns_game.gui.widgets.stacked_widget import StackedWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class PlayersSpaceUi(StackedWidget):
    """ The space on the tabletop where all player boards are displayed.

    This is a stacked widget as the layout used depends on whose turn it is. """

    overview_view: Widget
    # TODO -> the current player views should be a list of tuples with players to uis (or similar) so it's easy to
    #  determine which corresponds to what player.
    current_player_view: Widget

    def __init__(self, all_players: AllPlayers, **kwargs):
        self.overview_view = Label("All players!")
        self.current_player_view = Label("first player view")
        super().__init__(
            children=[
                self.overview_view,
                self.current_player_view,
            ],
            **kwargs)

    def change_players_view(self):
        if self.layout.currentWidget() == self.overview_view.widget:
            self.change_view(self.current_player_view)
        else:
            self.change_view(self.overview_view)
