from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.gui.players.cards_space import PlayerCardsSpace
from unstable_unicorns_game.gui.resources import style
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class PlayerUi:
    # Since the player information is stored here, I shouldn't need to rely on a dataclass wrapping it to a player
    # object.
    player: Player
    overview_view: ContainerWidget

    def __init__(self, player: Player, color_code: str):
        self.player = player
        self.overview_view = ContainerWidget(
            QHBoxLayout(),
            styling=style.player_space(color_code),
            children=[
                Label(player.name, style_identifier="name"),
                PlayerCardsSpace(player).view,
            ]
        )
