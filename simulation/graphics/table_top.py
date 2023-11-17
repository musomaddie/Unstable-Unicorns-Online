""" table top (center layout)"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from simulation.graphics.players_list import PlayersList
from simulation.graphics.utility import Widget


class TableTop(Widget):
    @classmethod
    def create_widget(cls, **kwargs) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QVBoxLayout())
        self.add_widgets(PlayersList.create_widget())
        # self.layout.addWidget()
