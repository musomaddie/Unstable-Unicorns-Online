""" card box """
from PyQt6.QtWidgets import QWidget


class CardBox:
    """ Creates a rectangle which is a space for a card box."""

    def __init__(self):
        self.box = QWidget()
        self.box.setFixedSize(64, 104)
        self.box.setStyleSheet("""
            background-color: #C0C0C0;
            border-style: dashed;
            border-radius: 5px;
            border-width: 2px;
            border-color: black;""")

    @classmethod
    def create_widget(cls) -> QWidget:
        """ Creates and returns the widget!"""
        return cls().box
