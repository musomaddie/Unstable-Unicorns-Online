"""
TKINTER practice
https://tkdocs.com/tutorial/grid.html
"""

import tkinter as tk
from tkinter import ttk

from simulation.graphics.main_game_board_frame import MainGameBoardFrame
from simulation.graphics.orientation import Orientation
from simulation.graphics.player_frame import PlayerFrame


class TableTopLayout:
    """
    Manages the main window (root layout) for the simulation.
    """

    def __init__(self, parent: tk.Tk):
        self.parent = parent
        self.content = ttk.Frame(parent)
        self.content.grid(column=0, row=0, sticky="NSEW")

        self.main_board = MainGameBoardFrame(self.content)
        self.main_board.root_frame.grid(column=1, row=1, sticky="NSEW")

        # TODO -> replace the following two lines with their own class.
        self.corners = [tk.Frame(self.content, width=50, height=50, borderwidth=2, relief="sunken") for _ in range(4)]
        self.setup_corners()

        self.players = [
            PlayerFrame(self.content, name, Orientation.HORIZONTAL if index % 2 == 0 else Orientation.VERTICAL)
            for index, name in enumerate(["Aelin", "Brannon", "Chaol", "Dorian"])]
        self.position_players()

        self.resize_config()

    def setup_corners(self):
        """ Positions the corners correctly. """
        self.corners[0].grid(column=0, row=0, sticky="NSEW")
        self.corners[1].grid(column=2, row=0, sticky="NSEW")
        self.corners[2].grid(column=2, row=2, sticky="NSEW")
        self.corners[3].grid(column=0, row=2, sticky="NSEW")

    def position_players(self):
        """ Positions player frames. """
        for frame, pos in zip(self.players, [(1, 0), (2, 1), (1, 2), (0, 1)]):
            frame.root.grid(column=pos[0], row=pos[1], sticky="NSEW")

    def resize_config(self):
        """ Sets up weights (and other stuff) to support resizing the window. """
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        for i in range(3):
            self.content.rowconfigure(i, weight=1)
            self.content.columnconfigure(i, weight=1)


if __name__ == '__main__':
    TableTopLayout()
