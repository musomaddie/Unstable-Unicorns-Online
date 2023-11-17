""" runs the simulation as a game. """
import sys

from PyQt6.QtWidgets import QApplication

from game_details.card import Card
from game_details.deck import Deck
from game_details.game_runner import Game
from game_details.nursery import Nursery
from simulation import MainWindow


def start_sim():
    """ Actually starts the simulation. """
    # Make game object.
    player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]
    my_deck = Deck([Card.create_card(
        {
            "name": "Basic Unicorn",
            "type": "basic unicorn",
            "text": "basic unicorn text :O"
        }) for _ in range(70)
    ])

    game = Game.create_game(player_names, my_deck, Nursery.create_default())

    # Start graphics.
    app = QApplication(sys.argv)
    window = MainWindow(game)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start_sim()
