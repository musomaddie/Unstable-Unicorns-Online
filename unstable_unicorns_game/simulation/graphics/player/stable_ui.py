""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.cards import CardsRow
from unstable_unicorns_game.simulation.graphics.widget.label import RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import CARD_HEIGHT, CARD_WIDTH, ContainerWidget, \
    GROUP_STYLES


def create_expanded_view(stable: Stable) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    cards_wid = CardsRow(stable.unicorns + stable.upgrades + stable.downgrades)

    widget.style_with_selectors(GROUP_STYLES["player_board_labels"])
    widget.add_widgets(
        RightAlignedLabel("Stable", style_identifier="lbl"),
        cards_wid
    )
    cards_wid.layout.setAlignment(cards_wid.widget, Qt.AlignmentFlag.AlignLeft)

    return widget


def create_compact_view(stable: Stable) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout(), style_identifier="container")
    # TODO -> this should actually be somewhat visible -> group by unicorns (type) and up / down grades.
    widget.size(CARD_WIDTH, CARD_HEIGHT)
    widget.style_with_selectors({
        "*": {
            "background-color": "#00CCCC",
        },
        "#container": {
            "border-style": "dashed",
            "border-radius": "2px",
            "border-width": "2px",
            "border-color": "black"
        }})

    return widget


class StableUi:
    stable: Stable

    expanded_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable

        self.expanded_view = create_expanded_view(stable)
        self.compact_view = create_compact_view(stable)
