""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QHBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUiType, CardUi
from unstable_unicorns_game.simulation.graphics.widget import GROUP_STYLES
from unstable_unicorns_game.simulation.graphics.widget import Widget


class StableCards(Widget):
    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())
        self.widget.setObjectName("cards")
        self.add_widgets(
            *[
                CardUi(CardUiType.from_card(card), card).widget
                for card in stable.unicorns + stable.upgrades + stable.downgrades
            ]
        )


class StableArea(Widget):
    def __init__(self, stable: Stable):
        super().__init__(QHBoxLayout())

        self.style_with_selectors(GROUP_STYLES["player_board_labels"])

        stable_lbl = QLabel("Stable")
        stable_lbl.setObjectName("lbl")
        stable_lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        cards = StableCards(stable).widget
        self.add_widgets(stable_lbl, cards)

        self.layout.setAlignment(cards, Qt.AlignmentFlag.AlignLeft)
