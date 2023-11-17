""" nursery area """
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from simulation.graphics.card_box import CardBox
from simulation.graphics.utility import Widget


class NurseryArea(Widget):

    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.style({"background-color": "#e34d61"})

        lbl = QLabel("Nursery")
        card_space = CardBox.create_widget()
        self.add_widgets(lbl, card_space)
