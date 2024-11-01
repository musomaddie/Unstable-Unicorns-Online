""" runs the simulation as a game. """
import sys

from PyQt6.QtWidgets import QApplication

from unstable_unicorns_game.game_details import game_factory
from unstable_unicorns_game.play_deciders import DeciderType, DeciderFactory
from unstable_unicorns_game.simulation import MainWindow


def start_sim():
    """ Actually starts the simulation. """
    # TODO -> make sure this actually makes sense with everything else that's going on.
    # Make game object.
    player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]
    this_game = game_factory.create(player_names, DeciderFactory(DeciderType.QUEUE))

    # Start graphics.
    app = QApplication(sys.argv)
    window = MainWindow(this_game)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_sim()
