""" Runs the simulation. """
import sys

from PyQt6.QtWidgets import QApplication

from simulation.graphics.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
