from dataclasses import dataclass

from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.gui.widgets.widget import Widget


@dataclass
class PlayerWithUi:
    player: Player
    ui: Widget
