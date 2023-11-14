""" Card deck canvas."""
import tkinter as tk
from tkinter import ttk


class CardDeckCanvas:
    """ a dotted rectangle outline for a card deck. """

    def __init__(self, parent: ttk.Frame):
        self.root = tk.Canvas(parent, width=36, height=57)
        # calculated by golden rectangle calc. (https://www.omnicalculator.com/math/golden-rectangle)
        # TODO consider putting these values in a top level file.
        # TODO -> make this look prettier.
        self.root.create_rectangle(3, 3, 33, 52, fill="grey75", outline="grey25", width=2, dash=(2,))
