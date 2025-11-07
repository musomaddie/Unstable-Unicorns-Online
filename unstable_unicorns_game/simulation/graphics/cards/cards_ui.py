from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUi
from unstable_unicorns_game.simulation.graphics.widget.widget import ContainerWidget


def create_row_of_cards(cards: list[Card]) -> ContainerWidget:
    widget = ContainerWidget(QHBoxLayout(), style_identifier="cards-row")
    widget.add_widgets(
        *[CardUi(card) for card in cards]
    )

    return widget
