from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLayout, QWidget

from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget


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

    def append_widget(self, widget: Widget):
        # NOTE -> be careful!
        self.layout.addWidget(widget.widget)
        self.children.append(widget)

    def add_widgets(self, *widgets: Widget):
        """ Adds the widgets to this layout in the order they're passed. """
        # This doesn't actually add children, it overwrites them. Any children added in prior calls will not be updated
        # when it comes to relayout.
        [self.layout.addWidget(widget.widget) for widget in widgets]
        self.children = [widget for widget in widgets]

    def disable_stretching(self):
        """ The items in this layout will not stretch to fill available space.

        BE CAREFUL! This must happen after all widgets have been added.
        BE CAREFUL: only works on box layouts.
        """
        self.layout.addStretch()

    def teardown(self):
        """ Removes all widgets from this layout. """
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        self.clear_layout()

    def relayout(self):
        """ Adds the layout back to this widget. """
        for child in self.children:
            child.relayout()

        self.widget.setLayout(self.layout)
        self.add_widgets(*self.children)

    def align(self, alignment: Qt.AlignmentFlag):
        self.layout.setAlignment(alignment)

    def set_margins(self, left: int = None, top: int = None, right: int = None, bottom: int = None):
        """ Sets the margins for this layout. """
        current_margins = self.widget.layout().contentsMargins()
        if left is None:
            left = current_margins.left()
        if top is None:
            top = current_margins.top()
        if right is None:
            right = current_margins.right()
        if bottom is None:
            bottom = current_margins.bottom()
        self.widget.layout().setContentsMargins(left, top, right, bottom)

    def remove_margins(self):
        """ Removes all margins applied to this layout. """
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
