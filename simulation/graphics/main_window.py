""" main window """
from PyQt6.QtWidgets import QMainWindow

from simulation.graphics.player_board import PlayerBoard


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        player_board_widget = PlayerBoard.create_widget("Aelin")
        self.setCentralWidget(player_board_widget)
