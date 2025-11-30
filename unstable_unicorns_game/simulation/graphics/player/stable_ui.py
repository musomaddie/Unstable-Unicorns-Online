""" stable area! """
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardsRow
from unstable_unicorns_game.simulation.graphics.utility import colours, styles
from unstable_unicorns_game.simulation.graphics.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.simulation.graphics.widgets.label import CenteredLabel, Label, RightAlignedLabel


class StableCardsContainer(ContainerWidget):
    unicorns: MultipleCardsHolder
    upgrades: MultipleCardsHolder
    downgrades: MultipleCardsHolder

    def __init__(self, stable: Stable, layout: QLayout, **kwargs):
        self.unicorns = stable.unicorns
        self.upgrades = stable.upgrades
        self.downgrades = stable.downgrades
        super().__init__(layout, **kwargs)

    def update(self):
        pass


class GroupedCardPileToUi:
    card_callable: Callable[[], list[Card]]
    cards: list[Card]
    label: CenteredLabel
    ui: ContainerWidget  # TODO -> is this needed or can I just use the widget from the parent class here?

    def __init__(self, card_callable: Callable[[], list[Card]]):
        self.card_callable = card_callable
        self.cards = card_callable()
        self.label = CenteredLabel(str(len(self.cards)))

        self.ui = ContainerWidget(QVBoxLayout(), style_identifier="container")

        # TODO -> only show if has a card, and hide otherwise.
        self.ui.set_size(styles.CARD_WIDTH, styles.CARD_HEIGHT)
        self.ui.style_with_selectors(styles.compact_card_pile_player(colours.baby_unicorn_pink))
        self.ui.add_widgets(self.label)


class StableCardsPile(StableCardsContainer):
    baby_unicorn_pile: GroupedCardPileToUi

    def __init__(self, stable: Stable, **kwargs):
        super().__init__(stable, QHBoxLayout(), style_identifier="container")

        overall_label = RightAlignedLabel("S: ", style_identifier="compact-lbl")
        self.baby_unicorn_pile = GroupedCardPileToUi(
            lambda: list(filter(lambda card: card.card_type == CardType.BABY_UNICORN, stable.unicorns)))

        self.add_widgets(
            overall_label,
            self.baby_unicorn_pile.ui)

        self.remove_margins()
        self.style_with_selectors(styles.player_ui_labels(True))


class StableCardsRow(StableCardsContainer):
    unicorns_row: CardsRow
    upgrades_row: CardsRow
    downgrades_row: CardsRow

    # unicorns_to_ui: list[CardToUi]
    # upgrades_to_ui: list[CardToUi]
    # downgrades_to_ui: list[CardToUi]
    #
    # unicorn_widget: ContainerWidget
    # upgrade_widget: ContainerWidget
    # downgrade_widget: ContainerWidget

    def __init__(self, stable: Stable, **kwargs):
        super().__init__(stable, layout=QHBoxLayout(), **kwargs)

        self.unicorns_row = CardsRow(stable.unicorns)
        self.upgrades_row = CardsRow(stable.upgrades)
        self.downgrades_row = CardsRow(stable.downgrades)

        # TODO -> is removing margins here defs correct?
        self.unicorns_row.remove_margins()
        self.upgrades_row.remove_margins()
        self.downgrades_row.remove_margins()

        self.add_widgets(
            self.unicorns_row, self.upgrades_row, self.downgrades_row)

    def update(self):
        self.unicorns_row.update()
        self.upgrades_row.update()
        self.downgrades_row.update()

        # TODO -> I might need to update the parent holder as well.


class StableContainerUi(ContainerWidget):
    stable: Stable
    cards_container: StableCardsContainer
    label: Label

    def __init__(self, cards_container: StableCardsContainer, label: Label, layout: QLayout, **kwargs):
        self.cards_container = cards_container
        self.label = label
        super().__init__(layout, **kwargs)

        self.add_widgets(label, cards_container)
        self.remove_margins()


def _create_expanded_view(stable: Stable) -> StableContainerUi:
    cards_container = StableCardsRow(stable)
    label = RightAlignedLabel("Stable", style_identifier="lbl")

    container = StableContainerUi(cards_container, label, QHBoxLayout())
    container.style_with_selectors(styles.player_ui_labels())

    return container


def _create_compact_view(stable: Stable) -> ContainerWidget:
    return StableCardsPile(stable)


def _create_turn_view(stable: Stable) -> StableContainerUi:
    cards_container = StableCardsRow(stable)
    cards_container.horizontal_stretch(1)
    label = CenteredLabel("Stable", style_identifier="cards-label")

    container = StableContainerUi(cards_container, label, QHBoxLayout())

    return container


class StableUi:
    stable: Stable

    expanded_view: StableContainerUi
    compact_view: ContainerWidget
    turn_view: StableContainerUi

    def __init__(self, stable: Stable):
        self.stable = stable

        self.expanded_view = _create_expanded_view(stable)
        self.compact_view = _create_compact_view(stable)
        self.turn_view = _create_turn_view(stable)
