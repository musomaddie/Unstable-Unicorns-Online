""" runs the simulation as a game. """
import sys

from PyQt6.QtWidgets import QApplication

from simulation import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
