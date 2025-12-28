from typing import Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLayout, QWidget

from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.widget import Widget


class ContainerWidget(Widget):
    """ Base class for widgets whose main purpose is to hold other widgets. """

    widget: QWidget
    layout: QLayout

    children: list[Widget]

    def __init__(
            self,
            layout: QLayout,
            children: Optional[list[Widget]] = None,
            spacing: Optional[int] = None,
            margins: Optional[Margins] = None,
            alignment: Optional[Qt.AlignmentFlag] = None,
            **kwargs):
        self.widget = QWidget()
        self.layout = layout
        self.widget.setLayout(layout)

        # The container widget itself adds margins. This can cause layout inconsistencies when multiple containers
        # are stacked, so remove these margins by default for simplicity. Extra margins can be applied through applied
        # styles or later adjustment of margins.
        # This has to be done prior to the super constructor being called so that any passed styling is not
        # overwritten. (I think ...)
        self.widget.layout().setContentsMargins(0, 0, 0, 0)
        # Remove additional spacing auto applied by horizontal / vertical layouts for the same reason as above.
        self.layout.setSpacing(0)

        super().__init__(self.widget, **kwargs)

        self.children = children or []
        if children is not None:
            self.add_widgets(*children)

        if spacing:
            self.set_spacing(spacing)
        if margins:
            self.set_margins(margins)
        if alignment:
            self.align(alignment)

    def add_widgets(self, *widgets: Widget):
        [self.layout.addWidget(widget.widget) for widget in widgets]
        self.children = [widget for widget in widgets]

    def set_spacing(self, spacing: int):
        self.layout.setSpacing(spacing)

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
