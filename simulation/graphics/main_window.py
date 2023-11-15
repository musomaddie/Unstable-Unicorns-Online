""" main window """
from PyQt6.QtWidgets import QMainWindow

from simulation.graphics.player_board import PlayerBoard


class MainWindow(QMainWindow):
    """ Runs the main window stuff. """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unstable Unicorn Game Simulation")

        player_board_widget = PlayerBoard()
        self.setCentralWidget(player_board_widget)

        # self.setWindowTitle("QDialog")

        # dialogLayout = QVBoxLayout()
        # formLayout = QFormLayout()
        # formLayout.addRow("Name:", QLineEdit())
        # formLayout.addRow("Age:", QLineEdit())
        # formLayout.addRow("Job:", QLineEdit())
        # formLayout.addRow("Hobbies:", QLineEdit())
        # dialogLayout.addLayout(formLayout)
        # buttons = QDialogButtonBox()
        # buttons.setStandardButtons(
        #     QDialogButtonBox.StandardButton.Cancel
        #     | QDialogButtonBox.StandardButton.Ok
        # )
        # dialogLayout.addWidget(buttons)
        # self.setLayout(dialogLayout)
        # self.view = TableAndMenuView()
        # self.view_widget = QWidget()
        # self.view_widget.setLayout(self.view)
        # self.setCentralWidget(self.view_widget)
