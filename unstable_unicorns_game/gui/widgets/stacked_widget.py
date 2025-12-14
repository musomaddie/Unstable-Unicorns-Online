from PyQt6.QtWidgets import QStackedLayout

from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class StackedWidget(ContainerWidget):
    """
    Variant of ContainerWidget where only one child is visible at a time.

    Roughly equivalent to QStackedLayout.
    """

    def __init__(self, **kwargs):
        super().__init__(QStackedLayout(), **kwargs)
