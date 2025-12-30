from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.gui.players.cards_space import PlayerCardsSpace
from unstable_unicorns_game.gui.resources import alignment, style
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class DetailedUi:
    # TODO -> choice label.

    view: ContainerWidget

    def __init__(self, name: str, cards_ui: PlayerCardsSpace, color_code: str):
        self.view = ContainerWidget(
            QVBoxLayout(),
            styling=style.player_space(color_code),
            children=[
                Label(
                    f"{name}'s turn",
                    style_identifier="turn-heading",
                    alignment=alignment.center(),
                    vertical_stretch=1),
                cards_ui.detailed_view
            ]
        )
        pass


class PlayerUi:
    # Since the player information is stored here, I shouldn't need to rely on a dataclass wrapping it to a player
    # object.
    player: Player

    cards_space: PlayerCardsSpace

    detailed_view: DetailedUi
    overview_view: ContainerWidget
    summary_view: ContainerWidget

    def __init__(self, player: Player, color_code: str):
        self.player = player
        self.cards_space = PlayerCardsSpace(player)
        # TODO -> improve stretch

        self.overview_view = ContainerWidget(
            QHBoxLayout(),
            styling=style.player_space(color_code),
            children=[
                Label(player.name, style_identifier="name", horizontal_stretch=1),
                self.cards_space.view
            ]
        )
        self.summary_view = ContainerWidget(
            QVBoxLayout(),
            children=[
                Label(player.name[0].upper(), style_identifier="initial", vertical_stretch=1),
                self.cards_space.compact_view],
            styling=style.player_space(color_code),
        )
        self.detailed_view = DetailedUi(player.name, self.cards_space, color_code)
