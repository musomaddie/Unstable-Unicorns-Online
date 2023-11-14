"""
TKINTER practice
https://tkdocs.com/tutorial/grid.html
"""

import tkinter as tk

from tkinter import ttk


class MainBoardFrame:
    def __init__(self, parent):
        self.root_frame = tk.Frame(parent)
        self.nursery_label = ttk.Label(self.root_frame, text="Nursery")
        self.nursery_label.pack()


class MainWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.content = ttk.Frame(self.root)
        self.main_board = ttk.Frame(self.content)
        self.corners = [tk.Frame(self.content, width=50, height=50, borderwidth=2, relief="sunken") for _ in range(4)]
        self.player_frames = [tk.Frame(self.content) for _ in range(4)]
        self.create_players()
        self.setup_rows()
        self.grid()
        self.resize_config()

        self.root.mainloop()

    def setup_rows(self):
        """ puts items in the grid by rows. """
        first_row = [self.corners[0], self.player_frames[0], self.corners[1]]
        second_row = [self.player_frames[3], self.main_board, self.player_frames[1]]
        third_row = [self.corners[3], self.player_frames[2], self.corners[2]]
        [item.grid(column=i, row=0, sticky="NSEW") for i, item in enumerate(first_row)]
        [item.grid(column=i, row=1, sticky="NSEW") for i, item in enumerate(second_row)]
        [item.grid(column=i, row=2, sticky="NSEW") for i, item in enumerate(third_row)]

    def grid(self):
        """ put all the layouts into the grid. """
        self.content.grid(column=0, row=0, sticky="NSEW")

    def create_players(self):
        """ Creates player objects. """

        player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]
        player_labels = [ttk.Label(fr, text=name) for fr, name in zip(self.player_frames, player_names)]
        [label.grid() for label in player_labels]

    def resize_config(self):
        """ Sets up weights (and other stuff) to support resizing the window. """
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        for i in range(3):
            self.content.rowconfigure(i, weight=1)
            self.content.columnconfigure(i, weight=1)


if __name__ == '__main__':
    MainWindow()
