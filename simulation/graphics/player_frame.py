""" player frame layout """
from tkinter import ttk

from simulation.graphics.orientation import Orientation


class PlayerFrame:
    """ Sets up the frame layout for a player. """

    def __init__(self, parent: ttk.Frame, player_name: str, orientation: Orientation):
        self.root = ttk.Frame(parent)
        name_lbl = ttk.Label(self.root, text=player_name)
        name_lbl.grid()
