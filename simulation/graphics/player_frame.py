""" player frame layout """
from tkinter import ttk

from simulation.graphics.card_deck_canvas import CardDeckCanvas
from simulation.graphics.orientation import Orientation


class PlayerFrame:
    """ Sets up the frame layout for a player.

    # TODO - fix appearance of ascii art here.
    HORIZONTAL looks like:
    ------------------------------------
    |   name                           |
    ------------------------------------
    | hand                             |
    | c1 | c2 | c3 | c4 | c5 | c6 | c7 |
    ------------------------------------
    | stable                           |
    | unicorns                         |
    | c1 | c2 | c3 | c4 | c5 | c6 | c7 |
    | upgrades / downgrades            |
    | c1 ...                           |
    ------------------------------------

    VERTICAL looks like:
    --------------------------------
    |       name                   |
    --------------------------------
    | hand  | stable               |
    |       | unicorns | ups/downs |
    | c1    | c1       | c1        |
    | c2    | c2       | c2        |
    | c3    | c3       | c3        |
    | c4    | c4       | c4        |
    | c5    | c5       | c5        |
    | c6    | c6       | c6        |
    | c7    | c7       | c7        |
    --------------------------------
    """

    def __init__(self, parent: ttk.Frame, player_name: str, orientation: Orientation):
        self.root = ttk.Frame(parent)
        name_lbl = ttk.Label(self.root, text=player_name)
        name_lbl.grid(column=0, row=0, sticky="NSEW")
        self.create_hand(orientation)

    def create_hand(self, orientation: Orientation):
        """ creates the layout for the players hand."""
        # TODO - 'privatise' methods.
        hand_frame = ttk.Frame(self.root)
        hand_frame.grid(column=0, row=1, sticky="NSEW")

        lbl = ttk.Label(hand_frame, text="Hand")
        lbl.grid(column=0, row=0, sticky="NSEW")

        # TODO -> extract number 7.
        card_spots = [CardDeckCanvas(hand_frame) for _ in range(7)]
        # TODO - make dataclass to make these tuples easier to read.
        card_pos = [
            (i, 1) for i in range(7)] if orientation == Orientation.HORIZONTAL else [(0, i + 1) for i in range(7)]

        for canvas, pos in zip(card_spots, card_pos):
            canvas.root.grid(column=pos[0], row=pos[1], sticky="NSEW")
