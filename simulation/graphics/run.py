""" Runs the simulation. """
import sys

from PyQt6.QtWidgets import QApplication

from simulation.graphics.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
sys.exit(app.exec())

# root = tk.Tk()
# TableTopLayout(root)
# root.mainloop()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.showMaximized()
#     sys.exit(app.exec())
