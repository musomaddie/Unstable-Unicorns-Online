from PyQt6.QtWidgets import QPushButton

from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget


class Button(Widget):
    button: QPushButton

    def __init__(self, text: str, on_click):
        self.button = QPushButton(text)
        super().__init__(self.button)

        self.button.pressed.connect(lambda: on_click())
        self.style(styles.button())

    def update_text(self, text: str):
        self.button.setText(text)

    def disable(self):
        self.button.setEnabled(False)
