from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.gui.cards.cards_ui import CardsRowView
from unstable_unicorns_game.gui.resources import alignment
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class StableUi:
    stable: Stable
    unicorn_container: CardsRowView
    upgrade_container: CardsRowView
    downgrade_container: CardsRowView

    view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable
        self.unicorn_container = CardsRowView(stable.unicorns)
        self.downgrade_container = CardsRowView(stable.downgrades)
        self.upgrade_container = CardsRowView(stable.upgrades)
        self.view = ContainerWidget(
            QHBoxLayout(), children=[
                Label("Stable", alignment=alignment.right()),
                self.unicorn_container, self.upgrade_container, self.downgrade_container],
            style_identifier="container",
            margins=Margins(top=10, bottom=10)
        )
