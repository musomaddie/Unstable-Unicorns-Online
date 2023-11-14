""" Main game board frame class. """
from tkinter import ttk

from simulation.graphics.card_deck_canvas import CardDeckCanvas


class MainGameBoardFrame:
    """ Manages the frame for the main game board. """

    def __init__(self, parent: ttk.Frame):
        self.root_frame = ttk.Frame(parent)
        self.setup_nursery()

        # Applied to parent object.
        self.root_frame.grid(column=1, row=1, sticky="NSEW")

    def setup_nursery(self):
        """ setups the nursery. """
        lbl = ttk.Label(self.root_frame, text="Nursery")
        canvas = CardDeckCanvas(self.root_frame)
        lbl.grid(column=0, row=0, sticky="NSEW")
        canvas.root.grid(column=0, row=1, sticky="NSEW")
