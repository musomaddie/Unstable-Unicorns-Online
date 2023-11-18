""" layout for main board area. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QWidget

from simulation.graphics.table_center.deck_area import DeckArea
from simulation.graphics.table_center.discard_area import DiscardArea
from simulation.graphics.table_center.nursery_area import NurseryArea
from simulation.graphics.utility import Widget


class TableCenter(Widget):

    @classmethod
    def create_widget(cls) -> QWidget:
        return cls().widget

    def __init__(self):
        super().__init__(QHBoxLayout())
        self.style({
            "font-family": "Permanent Marker",
            "font-size": "20px",
        })
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_widgets(
            NurseryArea.create_widget(),
            DeckArea().create_widget(),
            DiscardArea().create_widget()
        )
