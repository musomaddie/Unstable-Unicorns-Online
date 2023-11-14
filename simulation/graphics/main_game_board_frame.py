""" Main game board frame class. """
from tkinter import ttk

from simulation.graphics.card_deck_canvas import CardDeckCanvas


class MainGameBoardFrame:
    """ Manages the frame for the main game board. """

    def __init__(self, parent: ttk.Frame):
        self.root_frame = ttk.Frame(parent)

        self.setup_nursery()
        self.setup_deck()
        self.setup_discard_pile()

    def setup_nursery(self):
        """ setups the nursery. """
        lbl = ttk.Label(self.root_frame, text="Nursery")
        canvas = CardDeckCanvas(self.root_frame)
        lbl.grid(column=0, row=0, sticky="NSEW")
        canvas.root.grid(column=0, row=1, sticky="NSEW")

    def setup_deck(self):
        """ setups the deck (draw pile) """
        lbl = ttk.Label(self.root_frame, text="Deck (draw pile)")
        canvas = CardDeckCanvas(self.root_frame)
        lbl.grid(column=1, row=0, sticky="NSEW")
        canvas.root.grid(column=1, row=1, sticky="NSEW")

    def setup_discard_pile(self):
        """ setups the discard pile. """
        lbl = ttk.Label(self.root_frame, text="Discard pile")
        canvas = CardDeckCanvas(self.root_frame)
        lbl.grid(column=2, row=0, sticky="NSEW")
        canvas.root.grid(column=2, row=1, sticky="NSEW")