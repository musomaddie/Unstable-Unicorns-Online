""" widget class (different from QWidget) to form the base of my classes. """
from abc import abstractmethod

from PyQt6.QtWidgets import QWidget


class Widget:
    """ Base class for all my widgets.

    Extend this instead of extending QWidget() directly so that setStyleSheet() works.
    """
    widget: QWidget

    def __init__(self):
        # TODO - add layout here
        self.widget = QWidget()

    def style(self, style_dictionary: dict[str, dict[str, str]]):
        """ Applies the given style dictionary to this widget. """
        selectors = []
        for selector, style in style_dictionary.items():
            selector_str = f"{selector} {{"
            for key, value in style.items():
                selector_str += f"{key}: {value};"
            selector_str += "}"
            selectors.append(selector_str)
            # selectors.append(f"{selector} {{")
        # styles = [f"{key}: {value};" for key, value in style_dictionary]
        self.widget.setStyleSheet(
            "\n".join(selectors)
        )

    @classmethod
    @abstractmethod
    def create_widget(cls, **kwargs) -> QWidget:
        """ Returns the widget for this class. """
        pass
