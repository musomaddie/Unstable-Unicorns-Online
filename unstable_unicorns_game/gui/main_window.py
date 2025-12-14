from PyQt6.QtWidgets import QHBoxLayout, QMainWindow

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.tabletop.table_top import TableTopUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class MainWindow(QMainWindow):

    def __init__(self, game: Game):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game")

        board = BoardWidget(game)
        self.setCentralWidget(board.widget)


class BoardWidget(ContainerWidget):

    def __init__(self, game: Game):
        super().__init__(
            QHBoxLayout(),
            children=[TableTopUi(game).view]
        )
