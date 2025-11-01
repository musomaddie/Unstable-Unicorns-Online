""" widget class (different from QWidget) to form the base of my classes. """
from abc import ABC

from PyQt6.QtWidgets import QWidget, QLayout

GROUP_STYLES = {
    "card_piles": {
        "#container": {
            "border-style": "solid",
            "border-width": "3",
            "border-color": "navy",
            "border-radius": "20",
        },
    },
    "player_board_labels": {
        "#lbl": {
            "font-family": "Permanent Marker",
            "font-size": "20px",
            "border-right": "1px solid gray",
            "padding-right": "2px",
            "color": "gray"
        }
    }
}


# TODO -> move out of util and into top level graphics.
class Widget(ABC):
    """ Base class for all my widgets.

    Extend this instead of extending QWidget() directly so that setStyleSheet() works.
    """
    widget: QWidget

    def __init__(self, layout: QLayout):
        self.widget = QWidget()
        self.layout = layout
        self.widget.setLayout(layout)

    @staticmethod
    def _make_style_str(styles: dict[str, str]) -> str:
        return " ".join([f"{key}: {value};" for key, value in styles.items()])

    def style(self, style_dictionary: dict[str, str]):
        """ Applies a style without any selectors."""
        self.widget.setStyleSheet(self._make_style_str(style_dictionary))

    def style_with_selectors(self, style_dictionary: dict[str, dict[str, str]]):
        """ Applies the given style dictionary (including selectors) to this widget. """
        # TODO -> make this so the dictionary style sheet doesn't have to be passed in ?? the widget can just
        #  specifiy what it cares about, and then this can be responsible for handling that. ???
        selectors = []
        for selector, style in style_dictionary.items():
            selectors.append(f"{selector} {{ {self._make_style_str(style)} }}")
        self.widget.setStyleSheet(
            "\n".join(selectors)
        )

    def add_widgets(self, *widgets: QWidget):
        """ Adds the widgets to this layout in the order they're passed. """
        [self.layout.addWidget(widget) for widget in widgets]
