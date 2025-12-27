from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsRowView
from unstable_unicorns_game.gui.resources import alignment
from unstable_unicorns_game.gui.resources.measurement import Margins
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class StableUi:
    stable: Stable
    container: CardsContainerWithUi

    view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable

        stable_cards = stable.unicorns + stable.upgrades + stable.downgrades

        self.container = CardsContainerWithUi(
            stable_cards,
            label=Label("Stable", alignment=alignment.right()),
            container_view=CardsRowView(stable_cards),
            overall_view=ContainerWidget(
                QHBoxLayout(),
                style_identifier="container",
                margins=Margins(top=10, bottom=10)
            ))

        self.view = self.container.overall_view
