"""
TKINTER practice
https://tkdocs.com/tutorial/grid.html
"""

import tkinter as tk

from tkinter import ttk


class MainGameBoardFrame:
    """ Manages the frame for the main game board. """

    def __init__(self, parent):
        self.root_frame = tk.Frame(parent)
        self.nursery_label = ttk.Label(self.root_frame, text="Nursery")
        self.nursery_label.pack()


class MainWindow:
    """
    Manages the main window (root layout) for the simulation.
    """

    def __init__(self):
        # TODO -> consider putting root somewhere else and just having this class have the frame.
        self.root = tk.Tk()

        self.content = ttk.Frame(self.root)
        self.content.grid(column=0, row=0, sticky="NSEW")

        # TODO -> replace the following two lines with their own class.
        self.main_board = ttk.Frame(self.content)
        self.setup_main_board()

        # TODO -> replace the following two lines with their own class.
        self.corners = [tk.Frame(self.content, width=50, height=50, borderwidth=2, relief="sunken") for _ in range(4)]
        self.setup_corners()

        # TODO -> replace the following two lines with their own class.
        self.player_frames = [tk.Frame(self.content) for _ in range(4)]
        self.setup_players()

        self.resize_config()

        # TODO -> consider making a "run" method (?)
        self.root.mainloop()

    def setup_main_board(self):
        """ Sets up stuff for the main board. """
        # We already have the frame layout created in the init. (I don't think there's really any nice way around this).
        self.main_board.grid(column=1, row=1, sticky="NSEW")

    def setup_corners(self):
        """ Positions the corners correctly. """
        self.corners[0].grid(column=0, row=0, sticky="NSEW")
        self.corners[1].grid(column=2, row=0, sticky="NSEW")
        self.corners[2].grid(column=2, row=2, sticky="NSEW")
        self.corners[3].grid(column=0, row=2, sticky="NSEW")

    def setup_players(self):
        """ Setups player objects. """
        player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]
        player_labels = [ttk.Label(fr, text=name) for fr, name in zip(self.player_frames, player_names)]
        [label.grid() for label in player_labels]
        self.player_frames[0].grid(row=0, column=1, sticky="NSEW")
        self.player_frames[1].grid(row=1, column=2, sticky="NSEW")
        self.player_frames[2].grid(row=2, column=1, sticky="NSEW")
        self.player_frames[3].grid(row=1, column=0, sticky="NSEW")

    def resize_config(self):
        """ Sets up weights (and other stuff) to support resizing the window. """
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        for i in range(3):
            self.content.rowconfigure(i, weight=1)
            self.content.columnconfigure(i, weight=1)


if __name__ == '__main__':
    MainWindow()
