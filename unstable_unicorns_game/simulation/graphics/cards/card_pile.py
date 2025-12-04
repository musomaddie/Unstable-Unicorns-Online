""" The UI to represent a pile (stack) of cards. """
from PyQt6.QtWidgets import QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.utility import colours, styles
from unstable_unicorns_game.simulation.graphics.utility.measurements import CARD_SIZE
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel


def _create_card_pile(
        cards: list[Card],
        style_identifier: str,
        style_selectors) -> ContainerWidget:
    return ContainerWidget(
        QVBoxLayout(), style_identifier=style_identifier, styling=style_selectors,
        size=CARD_SIZE,
        children=[CenteredLabel(str(len(cards)))])


def create_center_card_pile(card_holder: MultipleCardsHolder) -> ContainerWidget:
    return _create_card_pile(card_holder.cards, "outline", styles.table_center_card_piles())


def create_player_compact_card_pile(cards: list[Card], colour: str = colours.grey) -> ContainerWidget:
    return _create_card_pile(cards, "container", styles.compact_card_pile_player(colour))
