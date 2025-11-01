from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.simulation.graphics.table_top import TableTop


class Controller:
    game: Game
    table_top: TableTop

    def __init__(self, game: Game, table_top: TableTop):
        # TODO -> consider if I want this to be a custom widget / button at all.
        # self.player_list = player_list
        self.game = game
        self.table_top = table_top

        button = QPushButton("Compact")
        # button.pressed.connect(lambda: self.on_compact_click())

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.widget = button

    # def on_compact_click(self):
    #     self.player_list.update_view_mode(TableViewMode.CURRENT_PLAYER)


"""
self.button = QPushButton(f"Click Count: {self.count}", self)
self.button.setFixedSize(120, 60)
self.button.clicked.connect(self.count_clicks)
layout = QVBoxLayout()
layout.addWidget(self.button)
self.setLayout(layout)

def count_clicks(self):
self.count += 1
self.button.setText(f"Click Count: {self.count}"""
