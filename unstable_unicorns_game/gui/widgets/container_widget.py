from typing import Optional

from PyQt6.QtWidgets import QLayout, QWidget

from unstable_unicorns_game.gui.widgets.widget import Widget


class ContainerWidget(Widget):
    """ Base class for widgets whose main purpose is to hold other widgets. """

    widget: QWidget
    layout: QLayout

    children: list[Widget]

    def __init__(self, layout: QLayout, children: Optional[list[Widget]] = None, **kwargs):
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

    def add_widgets(self, *widgets: Widget):
        [self.layout.addWidget(widget.widget) for widget in widgets]
        self.children = [widget for widget in widgets]
