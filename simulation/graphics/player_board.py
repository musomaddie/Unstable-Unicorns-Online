""" player board layout. """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout

from simulation.graphics.card_box import CardBox

MAX_HAND_SIZE = 7


class PlayerHand:
    """ Contains the hand area of a player board. """

    @staticmethod
    def _create_lbl():
        lbl = QLabel("Hand")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet(
            "background-color: #c7c1f5;"
        )
        return lbl

    @staticmethod
    def _create_cards():
        hand_cards = QHBoxLayout()
        hand_cards_widget = QWidget()
        hand_cards_widget.setLayout(hand_cards)
        hand_cards_widget.setStyleSheet(
            """background-color: #e5c1f5 """
        )
        for _ in range(MAX_HAND_SIZE):
            hand_cards.addWidget(CardBox.create_widget())
        return hand_cards_widget

    def __init__(self):
        self.widget = QWidget()
        hand_layout = QVBoxLayout()
        self.widget.setLayout(hand_layout)
        self.widget.setStyleSheet(
            """background-color: #f5c1f1;"""
        )

        hand_layout.addWidget(self._create_lbl())
        hand_layout.addWidget(self._create_cards())

    @classmethod
    def create_widget(cls) -> QWidget:
        """ creates and returns corresponding widget."""
        return cls().widget


class PlayerUnicorns:
    """ Does unicorns stuff. """

    @staticmethod
    def _create_lbl():
        lbl = QLabel("unicorns")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet(
            "background-color: #e3f5c1;"
        )
        return lbl

    @staticmethod
    def _create_cards():
        hand_cards = QHBoxLayout()
        hand_cards_widget = QWidget()
        hand_cards_widget.setLayout(hand_cards)
        hand_cards_widget.setStyleSheet(
            """background-color: #c1f5c1 """
        )
        for _ in range(MAX_HAND_SIZE):
            hand_cards.addWidget(CardBox.create_widget())
        return hand_cards_widget

    def __init__(self):
        self.widget = QWidget()
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.widget.setStyleSheet(
            "background-color: #f0f5c1;"
        )

        layout.addWidget(self._create_lbl())
        layout.addWidget(self._create_cards())

    @classmethod
    def create_widget(cls) -> QWidget:
        """ Creates and returns the corresponding widget. """
        return cls().widget


class PlayerStable:
    """ Contains the stable area of the board. """

    @staticmethod
    def _create_lbl():
        lbl = QLabel("Stable!")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl.setStyleSheet(
            "background-color: #f5cdc1;"
        )
        return lbl

    def __init__(self):
        self.widget = QWidget()
        self.widget.setStyleSheet(
            "background-color: #f5c1c6;"
        )
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self._create_lbl())
        layout.addWidget(PlayerUnicorns.create_widget())

    @classmethod
    def create_widget(cls) -> QWidget:
        """ returns the stable widget."""
        return cls().widget


class PlayerBoard:
    """ Contains the entire player board. """

    def __init__(self, player_name: str):
        board_layout = QVBoxLayout()
        card_contents = QHBoxLayout()
        card_contents_widget = QWidget()
        card_contents_widget.setStyleSheet(
            "background-color: #f5eac1;"
        )
        card_contents_widget.setLayout(card_contents)

        self.board = QWidget()
        self.board.setLayout(board_layout)
        self.board.setStyleSheet(
            "background-color: #c1d5f5;"
        )

        name_lbl = QLabel(player_name)
        name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        board_layout.addWidget(name_lbl)
        board_layout.addWidget(card_contents_widget)

        card_contents.addWidget(PlayerHand.create_widget())
        card_contents.addWidget(PlayerStable.create_widget())

    @classmethod
    def create_widget(cls, player_name: str) -> QWidget:
        """ Creates and returns the widget wrapping this. Used instead of having the class wrap the qwidget so that
        setStyleSheet works. """
        return cls(player_name).board

# class PlayerBoard(QWidget):
#     """ Contains an entire player board. """
#
#
#         info = QVBoxLayout()
#         info_wid = QWidget()
#         info_wid.setLayout(info)
#
#         hand_lbl = QLabel("Hand")
#         hand_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         hand_cards = QHBoxLayout()
#         hand_cards_widget = QWidget()
#         hand_cards_widget.setLayout(hand_cards)
#         for _ in range(7):
#             hand_cards.addWidget(CardBox.create_widget())
#
#         board_layout.addWidget(hand_lbl)
#         board_layout.addWidget(hand_cards_widget)
#
#         testing_label = QLabel("Testing")
#         testing_widget = QWidget()
#         testing_widget.setFixedSize(90, 100)
#         palette = testing_widget.palette()
#         palette.setColor(self.backgroundRole(), QColor("#bb22bb"))
#         testing_widget.setPalette(palette)
#         testing_widget.setAutoFillBackground(True)
#         board_layout.addWidget(testing_widget)
#         board_layout.addWidget(testing_label)
#
#         self.setLayout(board_layout)
