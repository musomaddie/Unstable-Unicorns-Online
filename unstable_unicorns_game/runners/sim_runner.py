import sys

from PyQt6.QtWidgets import QApplication

from unstable_unicorns_game.game_details.game.game import Game
from unstable_unicorns_game.play_deciders.factory import decider_factory
from unstable_unicorns_game.simulation import MainWindow


class SimulationRunner:
    def __init__(self):
        self._player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]

    def setup(self):
        """ Starts the game runner ... """
        # TODO -> move this into create_game() method (when it exists ... ). (and then add TODO regarding chosing
        #  number of players, names, etc.
        this_game = Game.create(self._player_names, decider_factory.create("queue"))

        app = QApplication(sys.argv)
        window = MainWindow(this_game)
        window.show()
        sys.exit(app.exec())


# FML -> we can't do it this way with the GUI because it will only respond to user events, so we can't have a shared
# runner calling methods, so each runner will have to call their own methods?

if __name__ == '__main__':
    runner = SimulationRunner()
    runner.setup()
