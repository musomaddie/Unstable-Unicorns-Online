from PyQt6.QtWidgets import QStackedLayout

from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class StackedWidget(ContainerWidget):
    """
    Variant of ContainerWidget where only one child is visible at a time.

    Roughly equivalent to QStackedLayout.
    """
    layout: QStackedLayout

    def __init__(self, **kwargs):
        self.layout = QStackedLayout()
        super().__init__(self.layout, **kwargs)

    def change_view(self, view: Widget):
        self.layout.setCurrentWidget(view.widget)
