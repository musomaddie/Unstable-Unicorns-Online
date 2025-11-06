from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel

from unstable_unicorns_game.simulation.graphics.widget.widget import Widget


class Label(Widget):
    label: QLabel

    def __init__(self, text: str, word_wrap: bool = False, **kwargs):
        self.label = QLabel(text)
        super().__init__(self.label, **kwargs)

        if word_wrap:
            self.label.setWordWrap(True)


class CenteredLabel(Label):
    def __init__(
            self,
            text: str,
            horizontal_align: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignVCenter,
            **kwargs):
        super().__init__(text, **kwargs)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter | horizontal_align)


class RightAlignedLabel(Label):
    def __init__(self, text: str, vertically_centered: bool = True, **kwargs):
        super().__init__(text, **kwargs)

        if vertically_centered:
            self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        else:
            self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
