"""
TKINTER practice
https://tkdocs.com/tutorial/grid.html
"""

import tkinter as tk

from tkinter import ttk

root = tk.Tk()

content = ttk.Frame(root)

corners = [tk.Frame(content, width=50, height=50, borderwidth=2, relief="sunken") for _ in range(4)]

main_board_frame = tk.Frame(content)

player_names = ["Aelin", "Brannon", "Chaol", "Dorian"]
player_frames = [tk.Frame(content) for _ in range(4)]
player_labels = [ttk.Label(fr, text=name) for fr, name in zip(player_frames, player_names)]
[label.grid() for label in player_labels]

content.grid(column=0, row=0, sticky="NSEW")

top_row = [corners[0], player_frames[0], corners[1]]
middle_row = [player_frames[3], main_board_frame, player_frames[1]]
last_row = [corners[2], player_frames[2], corners[3]]

[item.grid(column=i, row=0, sticky="NSEW") for i, item in enumerate(top_row)]
[item.grid(column=i, row=1, sticky="NSEW") for i, item in enumerate(middle_row)]
[item.grid(column=i, row=2, sticky="NSEW") for i, item in enumerate(last_row)]

# Configure to allow resizing.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)

root.mainloop()
