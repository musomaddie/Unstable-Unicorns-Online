""" player hand board area. """
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardsContainerUi, CardsPile, CardsRow
from unstable_unicorns_game.simulation.graphics.utility import styles
from unstable_unicorns_game.simulation.graphics.widgets.label import RightAlignedLabel


def _create_expanded_view(cards: MultipleCardsHolder) -> CardsContainerUi:
    widget = CardsContainerUi(
        cards_container=CardsRow(cards),
        label=RightAlignedLabel("Hand", style_identifier="lbl"),
        layout=QHBoxLayout())
    widget.style_with_selectors(styles.player_ui_labels())

    return widget


def _create_compact_view(cards: MultipleCardsHolder) -> CardsContainerUi:
    pile = CardsPile(
        cards, style_identifier="container", styling=styles.compact_card_pile_player())
    widget = CardsContainerUi(
        cards_container=pile,
        label=RightAlignedLabel("H: ", style_identifier="compact-lbl"),
        layout=QHBoxLayout()
    )
    widget.style_with_selectors(styles.player_ui_labels(True))

    return widget


def _create_turn_view(hand: Hand) -> CardsContainerUi:
    # TODO -> figure out how to make this update well once a card is drawn.
    cards_container = CardsRow(hand)
    cards_container.horizontal_stretch(1)
    widget = CardsContainerUi(
        cards_container,
        label=RightAlignedLabel("Hand", style_identifier="cards-label"),
        layout=QHBoxLayout())

    return widget


class HandUi:
    hand: Hand

    expanded_view: CardsContainerUi
    compact_view: CardsContainerUi
    turn_view: CardsContainerUi

    def __init__(self, hand: Hand):
        self.hand = hand

        self.expanded_view = _create_expanded_view(hand)
        self.compact_view = _create_compact_view(hand)
        self.turn_view = _create_turn_view(hand)

    def teardown_all(self):
        self.expanded_view.teardown()
        self.compact_view.teardown()
        self.turn_view.teardown()

    def update_view(self):
        self.expanded_view.cards_container.update()
        self.compact_view.cards_container.update()
        self.turn_view.cards_container.update()

    def enable_card_selection(self, on_click: Callable[[Card], None]):
        self.expanded_view.cards_container.enable_card_selection(on_click)
        self.compact_view.cards_container.enable_card_selection(on_click)
        self.turn_view.cards_container.enable_card_selection(on_click)

    def disable_card_selection(self):
        self.expanded_view.cards_container.disable_card_selection()
        self.compact_view.cards_container.disable_card_selection()
        self.turn_view.cards_container.disable_card_selection()
