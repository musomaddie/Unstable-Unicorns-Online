""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.utility import colours, styles
from unstable_unicorns_game.simulation.graphics.widget.label import CenteredLabel
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def _create_card_pile(
        cards: list[Card],
        style_identifier: str,
        style_selectors) -> ContainerWidget:
    widget = ContainerWidget(QVBoxLayout(), style_identifier=style_identifier)

    widget.set_size(styles.CARD_WIDTH, styles.CARD_HEIGHT)
    widget.style_with_selectors(style_selectors)

    widget.add_widgets(CenteredLabel(str(len(cards))))

    return widget


def create_center_card_pile(card_holder: MultipleCardsHolder) -> ContainerWidget:
    return _create_card_pile(card_holder.cards, "outline", styles.table_center_card_piles())


def create_player_compact_card_pile(cards: list[Card], colour: str = colours.grey) -> ContainerWidget:
    return _create_card_pile(cards, "container", styles.compact_card_pile_player(colour))
