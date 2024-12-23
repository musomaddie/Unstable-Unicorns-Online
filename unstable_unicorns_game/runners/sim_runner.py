import sys

from PyQt6.QtWidgets import QApplication

from unstable_unicorns_game.game_details.game.factory import game_factory
from unstable_unicorns_game.play_deciders.factory import decider_factory
from unstable_unicorns_game.runners.runner import Runner
from unstable_unicorns_game.simulation import MainWindow


class SimulationRunner(Runner):
    def __init__(self):
        self._player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]

    def setup(self):
        """ Starts the game runner ... """
        this_game = game_factory.create(self._player_names, decider_factory.create("queue"))

        app = QApplication(sys.argv)
        window = MainWindow(this_game)
        window.show()
        sys.exit(app.exec())


if __name__ == '__main__':
    runner = SimulationRunner()
    runner.run()
