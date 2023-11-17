""" main window """
from PyQt6.QtWidgets import QMainWindow

from simulation.graphics.table_top import TableTop


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        board_widget = TableTop.create_widget()
        self.setCentralWidget(board_widget)
