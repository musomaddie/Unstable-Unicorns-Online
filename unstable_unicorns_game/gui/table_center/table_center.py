from PyQt6.QtWidgets import QHBoxLayout, QLabel

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.resources.measurement import CENTER_CARD_PILE_SPACING
from unstable_unicorns_game.gui.table_center.center_pile_ui import CenterPileUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.widget import Widget


class TableCenterUi:
    view: ContainerWidget
    deck: CenterPileUi
    nursery: CenterPileUi

    def __init__(self, game: Game):
        self.deck = CenterPileUi(game.deck, "Deck")
        self.nursery = CenterPileUi(game.nursery, "Nursery")
        self.view = ContainerWidget(
            QHBoxLayout(),
            children=[
                Widget(widget=QLabel("Table Center")),
                self.deck.view,
                self.nursery.view,
            ],
            spacing=CENTER_CARD_PILE_SPACING,
        )
