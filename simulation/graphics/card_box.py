""" card box """
from PyQt6.QtWidgets import QWidget


def create_card_box():
    """ Creates a card box. """
    box = QWidget()
    box.setFixedSize(30, 40)
    box.setStyleSheet("""
        background-color: grey;
        border-style: solid;
        border-width: 4px;
        border-radius: 10px;
        border-color: black;""")

    return box


class CardBox(QWidget):
    """ card box widget """

    def __init__(self):
        super().__init__()
        # self.setAutoFillBackground(True)
        # w.setAttribute(QtCore.Qt.WA_StyledBackground)
        # self.setAttribute(Qt.WA_StyledBackground)

        self.setFixedSize(200, 300)
        self.setStyleSheet("background-color: yellow;")
        # testing_widget = QWidget()
        # testing_widget.setFixedSize(90, 100)
        # palette = testing_widget.palette()
        # palette.setColor(self.backgroundRole(), QColor("#bb22bb"))
        # testing_widget.setPalette(palette)
        # testing_widget.setAutoFillBackground(True)
        # board_layout.addWidget(testing_widget)
        # board_layout.addWidget(testing_label)
