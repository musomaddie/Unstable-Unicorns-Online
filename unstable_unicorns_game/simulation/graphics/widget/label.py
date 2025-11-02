from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from unstable_unicorns_game.simulation.graphics.widget.widget import Widget


class Label(Widget):
    label: QLabel

    def __init__(self, text: str, word_wrap: bool = False):
        self.label = QLabel(text)
        super().__init__(self.label)

        if word_wrap:
            self.label.setWordWrap(True)


class CenteredLabel(Label):
    def __init__(self, text: str, word_wrap: bool = False):
        super().__init__(text, word_wrap)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)


class RightAlignedLabel(Label):
    def __init__(self, text: str, vertically_centered: bool = True):
        super().__init__(text)

        if vertically_centered:
            self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        else:
            self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
