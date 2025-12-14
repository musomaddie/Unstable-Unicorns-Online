from typing import Optional

from PyQt6.QtWidgets import QWidget

import unstable_unicorns_game.gui.styles.general as gen_styles


class Widget:
    """ Base class for all my widgets.

    Extend this instead of extending QWidget() directly so that setStyleSheet() works consistently."""
    widget: QWidget

    def __init__(self, widget: Optional[QWidget] = None):
        if widget is None:
            widget = QWidget()
        self.widget = widget

        self.style_selectors(gen_styles.testing_border())

    @staticmethod
    def _make_style_str(styles: dict[str, str]) -> str:
        return " ".join([f"{key}: {value};" for key, value in styles.items()])

    def style(self, style_dictionary: dict[str, str]):
        """ Applies a style without any selectors."""
        self.widget.setStyleSheet(self._make_style_str(style_dictionary))

    def style_selectors(self, style_dictionary: dict[str, dict[str, str]]):
        """ Applies the given style dictionary (including selectors) to this widget. """
        # TODO -> make this so the dictionary style sheet doesn't have to be passed in ?? the widget can just
        #  specify what it cares about, and then this can be responsible for handling that. ???
        selectors = []
        for selector, style in style_dictionary.items():
            selectors.append(f"{selector} {{ {self._make_style_str(style)} }}")
        self.widget.setStyleSheet(
            "\n".join(selectors)
        )
