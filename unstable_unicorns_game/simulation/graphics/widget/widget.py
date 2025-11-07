""" widget class (different from QWidget) to form the base of my classes. """

from PyQt6.QtWidgets import QLayout, QWidget

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
            # "font-family": "Permanent Marker",
            "font-size": "20px",
            "border-right": "1px solid gray",
            "padding-right": "2px",
            "color": "gray"
        }
    }
}

# Prefer width 70, height 113 for golden rectangle, but manually setting to look alright on mac.
CARD_WIDTH = 72
CARD_HEIGHT = 104
SMALL_CARD_WIDTH = 36
SMALL_CARD_HEIGHT = 52


class Widget:
    """ Base class for all my widgets.

    Extend this instead of extending QWidget() directly so that setStyleSheet() works consistently.
    """
    widget: QWidget

    def __init__(self, widget: QWidget = None, style_identifier: str = None):
        if widget is None:
            widget = QWidget()
        self.widget = widget

        if style_identifier is not None:
            self.widget.setObjectName(style_identifier)

    @staticmethod
    def _make_style_str(styles: dict[str, str]) -> str:
        return " ".join([f"{key}: {value};" for key, value in styles.items()])

    def style(self, style_dictionary: dict[str, str]):
        """ Applies a style without any selectors."""
        self.widget.setStyleSheet(self._make_style_str(style_dictionary))

    def size(self, width: int, height: int):
        self.widget.setFixedSize(width, height)

    def horizontal_stretch(self, stretch: int):
        sp = self.widget.sizePolicy()
        sp.setHorizontalStretch(stretch)
        self.widget.setSizePolicy(sp)

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

    def clear_layout(self):
        """ Removes this widget from its layout. """
        self.widget.setParent(None)

    def relayout(self):
        # This widget doesn't have a layout, so there's nothing to do here. Including this method still to make relayout
        # in ContainerWidget easier.
        pass


class ContainerWidget(Widget):
    """
    Base class for widgets that have a layout. i.e. widgets that hold another widget.


    """
    widget: QWidget
    layout: QLayout

    children: list[Widget]

    def __init__(self, layout: QLayout, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.widget.setLayout(layout)

        self.children = []

    def add_widgets(self, *widgets: Widget):
        """ Adds the widgets to this layout in the order they're passed. """
        [self.layout.addWidget(widget.widget) for widget in widgets]
        self.children = [widget for widget in widgets]

    def teardown(self):
        """ Removes all widgets from this layout. """
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

    def relayout(self):
        """ Adds the layout back to this widget. """
        for child in self.children:
            child.relayout()

        self.widget.setLayout(self.layout)
        self.add_widgets(*self.children)
