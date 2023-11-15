""" player frame layout """
from dataclasses import dataclass
from enum import Enum

from tkinter import ttk

from simulation.graphics.card_deck_canvas import CardDeckCanvas
from simulation.graphics.utility import GridPosition


class PlayerFrame:
    """ Sets up the frame layout for a player.

    # TODO - fix appearance of ascii art here.
    HORIZONTAL gridded like:
    +----------------------------------------------+
    | +------------------------------------------+ |
    | | name                                     | |
    | -------------------------------------------- |
    | | hand                                     | |
    | | c1 | c2 | c3 | c4 | c5 | c6 | c7         | |
    | ---------------------------------------------|
    | | +--------------------------------------+ | |
    | | | stable                               | | |
    | | | +----------------------------------+ | | |
    | | | | unicorns                         | | | |
    | | | | c1 | c2 | c3 | c4 | c5 | c6 | c7 | | | |
    | | | ------------------------------------ | | |
    | | | | upgrades / downgrades            | | | |
    | | | | +------------------------------+ | | | |
    | | | | | c1 ...                       | | | | |
    | | | +----------------------------------+ | | |
    | | +--------------------------------------+ | |
    | +------------------------------------------+ |
    +----------------------------------------------+


    VERTICAL looks like:
    +--------------------------------------+
    | +----------------------------------+ |
    | | name                             | |
    | -------------------------------------|
    | | hand +-------------------------+ | |
    | | c1   | stable                  | | |
    | | c2   | +---------------------+ | | |
    | | c3   | | unicorns | up/down  | | | |
    | | c4   | | c1       | +------+ | | | |
    | | c5   | | c2       | | c1   | | | | |
    | | c6   | | c3       | | ...  | | | | |
    | | c7   | | c4       | +------+ | | | |
    | |      | | c5       |          | | | |
    | |      | | c6       |          | | | |
    | |      | | c7       |          | | | |
    | |      | +---------------------+ | | |
    | |      +-------------------------+ | |
    | +----------------------------------+ |
    +--------------------------------------+
    """
    max_hand_size = 7

    def __init__(self, parent: ttk.Frame, player_name: str, orientation: 'Orientation'):
        self.root = ttk.Frame(parent)
        name_lbl = ttk.Label(self.root, text=player_name, foreground="white")
        name_lbl.grid(column=0, row=0, sticky="NSEW")

        board_contents = ttk.Frame(self.root)
        board_contents.grid(column=0, row=1, sticky="NSEW")
        self.setup_hand(board_contents, orientation)
        self.setup_stable(board_contents, orientation)

    @staticmethod
    def setup_hand(board_contents, orientation):
        """ setup hand """
        # Hand contents
        hand_frame = ttk.Frame(board_contents)
        hand_frame.grid(column=0, row=0, sticky="NSEW")

        hand_lbl = ttk.Label(hand_frame, text="Hand", foreground="blue")
        hand_lbl.grid(column=0, row=0, sticky="NSEW")

        hand_cards_frame = ttk.Frame(hand_frame)
        hand_cards_frame.grid(
            column=0,
            row=1,
            sticky="NSEW",
        )
        card_placeholders = [CardDeckCanvas(hand_cards_frame) for _ in range(7)]
        for canvas, position in zip(card_placeholders, orientation.value.cards_position):
            canvas.root.grid(
                column=position.col,
                row=position.row,
                sticky="NSEW",
            )

    def setup_stable(self, board_contents, orientation):
        """ setup stable. """
        stable_frame = ttk.Frame(board_contents)
        stable_frame.grid(
            column=orientation.value.stable_frame_position.col,
            row=orientation.value.stable_frame_position.row,
            sticky="NSEW",
        )

        stable_lbl = ttk.Label(stable_frame, text="Stable", foreground="purple")
        stable_lbl.grid(column=0, row=0, sticky="NSEW")

        self.setup_unicorns(stable_frame, orientation)

    @staticmethod
    def setup_unicorns(stable_contents, orientation):
        """ setup unicorns """
        unicorn_frame = ttk.Frame(stable_contents)
        unicorn_frame.grid(column=0, row=1, sticky="NSEW")

        unicorn_lbl = ttk.Label(unicorn_frame, text="Unicorns", foreground="navy")
        unicorn_lbl.grid(column=0, row=0, sticky="NSEW")

        unicorn_cards_frame = ttk.Frame(unicorn_frame)
        unicorn_cards_frame.grid(column=0, row=1, sticky="NSEW")
        card_placeholders = [CardDeckCanvas(unicorn_cards_frame) for _ in range(7)]
        for canvas, position in zip(card_placeholders, orientation.value.cards_position):
            canvas.root.grid(column=position.col, row=position.row, sticky="NSEW")


@dataclass
class Value:
    stable_frame_position: GridPosition
    cards_position: list[GridPosition]


class Orientation(Enum):
    # Longest side is <-- left, right -->
    HORIZONTAL = Value(
        stable_frame_position=GridPosition(row=3),
        cards_position=[GridPosition(col=i, row=1) for i in range(7)],
    )

    # Longest side is top to bottom
    VERTICAL = Value(
        stable_frame_position=GridPosition(col=2),
        cards_position=[GridPosition(col=0, row=i) for i in range(7)],
    )
