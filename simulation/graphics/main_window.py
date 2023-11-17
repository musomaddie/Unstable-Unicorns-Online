""" main window """
from PyQt6.QtWidgets import QMainWindow

from simulation.graphics.players_list import PlayersList


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        player_board_widget = PlayersList.create_widget()
        self.setCentralWidget(player_board_widget)
