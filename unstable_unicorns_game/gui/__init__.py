import sys

from PyQt6.QtWidgets import QApplication

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.main_window import MainWindow
from unstable_unicorns_game.play_deciders.queue_decider import QueueDecider


def setup():
    player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]

    this_game = Game.create(player_names, QueueDecider())

    app = QApplication(sys.argv)
    window = MainWindow(this_game)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    setup()
