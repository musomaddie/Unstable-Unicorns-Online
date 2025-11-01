""" main window """
from PyQt6.QtWidgets import QMainWindow

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.game_widget import GameWidget


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self, game: Game):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        board_widget = GameWidget(game).widget
        self.setCentralWidget(board_widget)
