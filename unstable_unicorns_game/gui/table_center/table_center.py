from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.game import Game
from unstable_unicorns_game.gui.resources.measurement import CENTER_CARD_PILE_SPACING
from unstable_unicorns_game.gui.table_center.center_pile_ui import CenterPileUi
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget


class TableCenterUi:
    view: ContainerWidget
    deck: CenterPileUi
    nursery: CenterPileUi
    discard: CenterPileUi

    def __init__(self, game: Game):
        # TODO -> change the spread behaviour when the window is resized.
        self.deck = CenterPileUi(game.deck, "Deck")
        self.nursery = CenterPileUi(game.nursery, "Nursery")
        self.discard = CenterPileUi(game.discard_pile, "Discard Pile")
        self.view = ContainerWidget(
            QHBoxLayout(),
            children=[
                self.deck.view,
                self.nursery.view,
                self.discard.view,
            ],
            spacing=CENTER_CARD_PILE_SPACING,
        )
