""" table top (center layout)"""

from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.players_list import PlayersList
from unstable_unicorns_game.simulation.graphics.table_center.table_center import TableCenter
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget

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
    center: TableCenter
    players: PlayersList

    def __init__(self, game: Game):
        super().__init__(QVBoxLayout())

        self.center = TableCenter(game)
        self.players = PlayersList(game.players)

        self.add_widgets(self.center, self.players)
