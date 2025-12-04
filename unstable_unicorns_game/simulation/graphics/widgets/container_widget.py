from typing import Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLayout, QWidget

from unstable_unicorns_game.simulation.graphics.utility.measurements import Margins
from unstable_unicorns_game.simulation.graphics.widgets.widget import Widget


class ContainerWidget(Widget):
    """
    Base class for widgets that have a layout. i.e. widgets that hold another widget.


    """
    widget: QWidget
    layout: QLayout

    children: list[Widget]

    def __init__(
            self,
            layout: QLayout,
            children: Optional[list[Widget]] = None,
            align: Optional[Qt.AlignmentFlag] = None,
            margins: Optional[Margins] = None,
            remove_margins: bool = False,
            **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.widget.setLayout(layout)
        self.children = []

        if children is not None:
            self.add_widgets(*children)

        if align:
            self.align(align)
        if margins:
            self.set_margins(margins)
        if remove_margins:
            self.remove_margins()

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

    def set_margins(self, margins: Margins):
        current_margins = self.widget.layout().contentsMargins()
        self.widget.layout().setContentsMargins(
            margins.left if margins.left is not None else current_margins.left(),
            margins.top if margins.top is not None else current_margins.top(),
            margins.right if margins.right is not None else current_margins.right(),
            margins.bottom if margins.bottom is not None else current_margins.bottom()
        )

    def remove_margins(self):
        """ Removes all margins applied to this layout. """
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
