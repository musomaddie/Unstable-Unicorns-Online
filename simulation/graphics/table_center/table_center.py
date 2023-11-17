""" layout for main board area. """
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from simulation.graphics.utility import Widget


class TableCenter(Widget):

    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget
        pass

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.style({"background-color": "#ae7ceb"})
