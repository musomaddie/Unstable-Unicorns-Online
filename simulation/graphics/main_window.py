""" main window """
from PyQt6.QtWidgets import QMainWindow

from game_details.game import Game
from simulation.graphics.table_top import TableTop


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self, game: Game):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        board_widget = TableTop.create_widget(game)
        self.setCentralWidget(board_widget)
