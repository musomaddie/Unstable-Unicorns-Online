""" player frame layout """
from tkinter import ttk

from simulation.graphics.card_deck_canvas import CardDeckCanvas
from simulation.graphics.utility.orientation import Orientation


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
    max_hand_size = 7

    def __init__(self, parent: ttk.Frame, player_name: str, orientation: Orientation):
        self.root = ttk.Frame(parent)
        name_lbl = ttk.Label(self.root, text=player_name)
        name_lbl.grid(column=0, row=0, sticky="NSEW")
        self._create_hand(orientation)
        self._create_stable(orientation)

    def _create_hand(self, orientation: Orientation):
        """ creates the layout for the players hand."""
        hand_frame = ttk.Frame(self.root)
        hand_frame.grid(column=0, row=1, sticky="NSEW")

        lbl = ttk.Label(hand_frame, text="Hand", background="cyan")
        lbl.grid(column=0, row=0, sticky="NSEW", columnspan=orientation.value.label_colspan)

        card_spots = [CardDeckCanvas(hand_frame) for _ in range(self.max_hand_size)]
        for canvas, pos in zip(card_spots, orientation.value.hand_card_pos):
            canvas.root.grid(column=pos.col, row=pos.row, sticky="NSEW")

    def _create_stable(self, orientation: Orientation):
        """ Creates a stable layout. """
        stable_frame = ttk.Frame(self.root)
        stable_frame.grid(
            column=orientation.value.stable_pos.col,
            row=orientation.value.stable_pos.row,
            sticky="NSEW",
            columnspan=orientation.value.stable_colspan)

        stable_lbl = ttk.Label(stable_frame, text="Stable", background="#3344ff")
        stable_lbl.grid(column=0, row=0, sticky="NSEW", columnspan=orientation.value.stable_colspan)

        unicorn_frame = ttk.Frame(stable_frame)
        unicorn_frame.grid(column=0, row=1, sticky="NSEW")
        unicorn_lbl = ttk.Label(unicorn_frame, text="Unicorns", background="#33ff22")
        unicorn_lbl.grid(column=0, row=0, sticky="NSEW", columnspan=orientation.value.label_colspan)
