from typing import Optional

from PyQt6.QtWidgets import QWidget

import unstable_unicorns_game.gui.resources.style as gen_styles
from unstable_unicorns_game.gui.resources.measurement import Size


class Widget:
    """ Base class for all my widgets.

    Extend this instead of extending QWidget() directly so that setStyleSheet() works consistently."""
    widget: QWidget

    def __init__(
            self,
            widget: Optional[QWidget] = None,
            style_identifier: Optional[str] = None,
            styling: Optional[dict[str, dict[str, str]]] = None,
            size: Optional[Size] = None,
            horizontal_stretch: Optional[int] = None,
            vertical_stretch: Optional[int] = None):
        if widget is None:
            widget = QWidget()
        self.widget = widget
        self.style_selectors(gen_styles.testing_border())

        if style_identifier:
            self.widget.setObjectName(style_identifier)
        if styling:
            self.style_selectors(styling)

        if size:
            self.set_size(size)
        if horizontal_stretch:
            self.horizontal_stretch(horizontal_stretch)
        if vertical_stretch:
            self.vertical_stretch(vertical_stretch)

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
            "\n".join(selectors))

    def set_size(self, size: Size):
        self.widget.setFixedSize(size.width, size.height)

    def horizontal_stretch(self, stretch: int):
        sp = self.widget.sizePolicy()
        sp.setHorizontalStretch(stretch)
        self.widget.setSizePolicy(sp)

    def vertical_stretch(self, stretch: int):
        sp = self.widget.sizePolicy()
        sp.setVerticalStretch(stretch)
        self.widget.setSizePolicy(sp)
