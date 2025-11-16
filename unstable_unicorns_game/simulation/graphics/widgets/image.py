from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget


class Image(Widget):
    image: QPixmap
    containerLabel: QLabel

    # self.widget = containerLabel in this case.

    def __init__(self, fn: str):
        self.image = QPixmap(fn)
        self.containerLabel = QLabel()
        self.containerLabel.setPixmap(self.image)
        super().__init__(self.containerLabel)
