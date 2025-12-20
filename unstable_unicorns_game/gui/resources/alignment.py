""" functions that just return a QT alignment, so I don't have to remember what it is each time."""
from PyQt6.QtCore import Qt


def center():
    return Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
