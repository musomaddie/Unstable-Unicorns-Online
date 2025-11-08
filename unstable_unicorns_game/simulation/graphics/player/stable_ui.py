""" stable area! """
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.card_pile import create_player_compact_card_pile
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import create_row_of_cards
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widget.label import RightAlignedLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def _create_expanded_view(stable: Stable) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())
    cards_wid = create_row_of_cards(stable.unicorns + stable.upgrades + stable.downgrades)

    widget.style_with_selectors(styles.player_ui_labels())
    widget.add_widgets(
        RightAlignedLabel("Stable", style_identifier="lbl"),
        cards_wid
    )
    cards_wid.layout.setAlignment(cards_wid.widget, Qt.AlignmentFlag.AlignLeft)

    return widget


def _card_pile_styling(card_type: CardType) -> dict[str, dict[str, str]]:
    pass


def _create_compact_unicorns(unicorns: MultipleCardsHolder) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout())

    # Attempt to create a view for each unicorn type.
    baby_unicorns = list(filter(lambda card: card.type == CardType.BABY_UNICORN, unicorns))
    if baby_unicorns:
        widget.add_widgets(
            create_player_compact_card_pile(baby_unicorns)
        )

    return widget


def _create_compact_view(stable: Stable) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout(), style_identifier="container")
    # TODO -> this should actually be somewhat visible -> group by unicorns (type) and up / down grades.
    widget.set_size(styles.CARD_WIDTH, styles.CARD_HEIGHT)
    widget.style_with_selectors(styles.compact_card_pile_for_player_hand())

    return widget


class StableUi:
    stable: Stable

    expanded_view: ContainerWidget
    compact_view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable

        self.expanded_view = _create_expanded_view(stable)
        self.compact_view = _create_compact_view(stable)
