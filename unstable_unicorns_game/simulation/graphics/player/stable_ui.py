""" stable area! """

from PyQt6.QtWidgets import QHBoxLayout, QLayout

from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardsGroupWithUi, CardsRow
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


class StableCardsPile(StableCardsContainer):
    baby_unicorn_pile: CardsGroupWithUi

    def __init__(self, stable: Stable, **kwargs):
        overall_label = RightAlignedLabel("S: ", style_identifier="compact-lbl")
        self.baby_unicorn_pile = CardsGroupWithUi(
            lambda: list(filter(lambda card: card.card_type == CardType.BABY_UNICORN, stable.unicorns)),
            styling=styles.compact_card_pile_player(colours.baby_unicorn_pink))

        super().__init__(
            stable,
            QHBoxLayout(),
            style_identifier="container",
            styling=styles.player_ui_labels(True),
            remove_margins=True,
            children=[overall_label, self.baby_unicorn_pile])


class StableCardsRow(StableCardsContainer):
    unicorns_row: CardsRow
    upgrades_row: CardsRow
    downgrades_row: CardsRow

    def __init__(self, stable: Stable, **kwargs):
        # TODO -> is removing margin defs correct??
        self.unicorns_row = CardsRow(stable.unicorns, remove_margins=True)
        self.upgrades_row = CardsRow(stable.upgrades, remove_margins=True)
        self.downgrades_row = CardsRow(stable.downgrades, remove_margins=True)

        super().__init__(
            stable,
            layout=QHBoxLayout(),
            children=[self.unicorns_row, self.upgrades_row, self.downgrades_row],
            **kwargs)

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
        super().__init__(layout, remove_margins=True, children=[label, cards_container], **kwargs)


def _create_expanded_view(stable: Stable) -> StableContainerUi:
    cards_container = StableCardsRow(stable)
    label = RightAlignedLabel("Stable", style_identifier="lbl")

    container = StableContainerUi(cards_container, label, QHBoxLayout(), styling=styles.player_ui_labels())

    return container


def _create_compact_view(stable: Stable) -> ContainerWidget:
    return StableCardsPile(stable)


def _create_turn_view(stable: Stable) -> StableContainerUi:
    cards_container = StableCardsRow(stable, horizontal_stretch=1)
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
