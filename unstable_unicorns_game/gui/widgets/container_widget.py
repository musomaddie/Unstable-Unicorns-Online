from typing import Optional

from PyQt6.QtWidgets import QLayout, QWidget

from unstable_unicorns_game.gui.widgets.widget import Widget


class ContainerWidget(Widget):
    """ Base class for widgets whose main purpose is to hold other widgets. """

    widget: QWidget
    layout: QLayout

    children: list[Widget]

    def __init__(self, layout: QLayout, children: Optional[list[Widget]] = None, **kwargs):
        super().__init__(**kwargs)
        self.layout = layout
        self.widget.setLayout(layout)

        self.children = children or []
        if children is not None:
            self.add_widgets(*children)

        # The container widget itself adds margins. This can cause layout inconsistencies when multiple containers
        # are stacked, so remove these margins by default for simplicity. Extra margins can be applied through applied
        # styles or later adjust of margins.
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def add_widgets(self, *widgets: Widget):
        [self.layout.addWidget(widget.widget) for widget in widgets]
        self.children = [widget for widget in widgets]
