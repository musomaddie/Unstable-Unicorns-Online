from PyQt6.QtWidgets import QPushButton, QVBoxLayout

from unstable_unicorns_game.simulation.graphics.players_list import ViewMode


class Controller:
    def __init__(self, player_list):
        # TODO -> probably turn this back into a custom widget
        self.player_list = player_list

        button = QPushButton("Compact")
        # button.clicked.connect(self.on_compact_click)
        button.pressed.connect(lambda: self.on_compact_click())

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.widget = button

    def on_compact_click(self):
        self.player_list.update_view_mode(ViewMode.CURRENT_PLAYER)


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
