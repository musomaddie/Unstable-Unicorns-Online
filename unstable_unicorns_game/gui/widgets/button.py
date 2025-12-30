from PyQt6.QtWidgets import QPushButton

from unstable_unicorns_game.gui.resources import style
from unstable_unicorns_game.gui.widgets.widget import Widget


class Button(Widget):
    button: QPushButton

    def __init__(self, text: str, on_click, **kwargs):
        self.button = QPushButton(text)
        super().__init__(self.button, **kwargs)

        self.button.pressed.connect(lambda: on_click())
        self.style(style.button())

    def update_text(self, text: str):
        self.button.setText(text)

    def disable(self):
        self.button.setEnabled(False)

    def enable(self):
        self.button.setEnabled(True)
