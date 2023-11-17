""" Card ui. """
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel

from simulation.graphics.utility import Widget


class CardUi(Widget):
    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.style({"background-color": "red"})

        # Attempt to put in an image
        image = QPixmap("simulation/graphics/images/card_types/unknown.png")
        label = QLabel()
        label.setPixmap(image)

        self.add_widgets(label)
