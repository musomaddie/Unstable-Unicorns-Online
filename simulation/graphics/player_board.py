""" player board layout. """
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

from simulation.graphics.card_box import create_card_box


class PlayerBoard(QWidget):
    def __init__(self, player_name: str):
        super().__init__()
        board_layout = QVBoxLayout()

        name_lbl = QLabel(player_name)
        board_layout.addWidget(name_lbl)
        board_layout.addWidget(create_card_box())

        info = QVBoxLayout()
        info_wid = QWidget()
        info_wid.setLayout(info)

        hand_lbl = QLabel("Hand")

        testing_label = QLabel("Testing")
        testing_widget = QWidget()
        testing_widget.setFixedSize(90, 100)
        palette = testing_widget.palette()
        palette.setColor(self.backgroundRole(), QColor("#bb22bb"))
        testing_widget.setPalette(palette)
        testing_widget.setAutoFillBackground(True)
        board_layout.addWidget(testing_widget)
        board_layout.addWidget(testing_label)

        self.setLayout(board_layout)

        # self.setFixedSize(30, 30)
        # palette = self.palette()
        # palette.setColor(self.backgroundRole(), QColor(222222))
        # self.setPalette(palette)
        # board_layout.addWidget()
