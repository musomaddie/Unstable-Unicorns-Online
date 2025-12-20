from typing import Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from unstable_unicorns_game.gui.widgets.widget import Widget


class Label(Widget):
    label: QLabel
    text: str

    def __init__(
            self, text: str, word_wrap: bool = False, alignment: Optional[Qt.AlignmentFlag] = None, **kwargs):
        self.label = QLabel(text)
        self.text = text
        super().__init__(self.label, **kwargs)

        if word_wrap:
            self.label.setWordWrap(True)

        if alignment:
            self.label.setAlignment(alignment)

    def update_text(self, text: str):
        self.text = text
        self.label.setText(text)
