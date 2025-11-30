""" stable area! """
from typing import Callable

from PyQt6.QtWidgets import QHBoxLayout, QLayout, QVBoxLayout

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.simulation.graphics.cards.card_ui import CardUi
from unstable_unicorns_game.simulation.graphics.cards.cards_ui import CardToUi
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
    # TODO -> can be simplified by making a container for widget + card to ui for each of unicorns / upgrades /
    #  downgrades.
    unicorns_to_ui: list[CardToUi]
    upgrades_to_ui: list[CardToUi]
    downgrades_to_ui: list[CardToUi]

    unicorn_widget: ContainerWidget
    upgrade_widget: ContainerWidget
    downgrade_widget: ContainerWidget

    def __init__(self, stable: Stable, **kwargs):
        super().__init__(stable, layout=QHBoxLayout(), **kwargs)

        self.unicorns_to_ui = [CardToUi(card, CardUi(card)) for card in stable.unicorns]
        self.upgrades_to_ui = [CardToUi(card, CardUi(card)) for card in stable.upgrades]
        self.downgrades_to_ui = [CardToUi(card, CardUi(card)) for card in stable.downgrades]

        self.unicorn_widget = ContainerWidget(QHBoxLayout(), style_identifier="cards-row")
        self.upgrade_widget = ContainerWidget(QHBoxLayout(), style_identifier="cards-row")
        self.downgrade_widget = ContainerWidget(QHBoxLayout(), style_identifier="cards-row")

        self.unicorn_widget.add_widgets(*[ui.ui for ui in self.unicorns_to_ui])
        self.upgrade_widget.add_widgets(*[ui.ui for ui in self.upgrades_to_ui])
        self.downgrade_widget.add_widgets(*[ui.ui for ui in self.downgrades_to_ui])
        self.unicorn_widget.remove_margins()
        self.upgrade_widget.remove_margins()
        self.downgrade_widget.remove_margins()

        self.add_widgets(*[self.unicorn_widget, self.upgrade_widget, self.downgrade_widget])

    def _add_missing_card_ui(
            self, missing_ui_list: list[CardToUi], corresponding_list: MultipleCardsHolder,
            changed_widget: ContainerWidget):
        ui_ids_list = [card_ui.card_id() for card_ui in missing_ui_list]
        for card in corresponding_list:
            if card.unique_id in ui_ids_list:
                continue
            new_card_ui = CardUi(card)
            changed_widget.append_widget(new_card_ui)
            missing_ui_list.append(CardToUi(card, new_card_ui))

            # TODO -> do we have to wipe the remaining ones too ??

    def update(self):
        if len(self.unicorns_to_ui) != self.unicorns:
            if len(self.unicorns) > len(self.unicorns_to_ui):
                self._add_missing_card_ui(self.unicorns_to_ui, self.unicorns, self.unicorn_widget)

        if len(self.upgrades_to_ui) != self.upgrades:
            if len(self.upgrades) > len(self.upgrades_to_ui):
                self._add_missing_card_ui(self.upgrades_to_ui, self.upgrades, self.upgrade_widget)

        if len(self.downgrades_to_ui) != self.downgrades:
            if len(self.downgrades) > len(self.downgrades_to_ui):
                self._add_missing_card_ui(self.downgrades_to_ui, self.downgrades, self.downgrade_widget)


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


def _create_expanded_view(stable: Stable):
    # Creates something that lets us update the cards in the stable. We need to link the cards to their UIs in a
    # sensible way.
    cards_container = StableCardsRow(stable)
    label = RightAlignedLabel("Stable", style_identifier="lbl")

    container = StableContainerUi(cards_container, label, QHBoxLayout())
    container.style_with_selectors(styles.player_ui_labels())

    return container


def _create_compact_view(stable: Stable) -> ContainerWidget:
    return StableCardsPile(stable)


def _create_turn_view(stable: Stable) -> ContainerWidget:
    cards_container = StableCardsRow(stable)
    cards_container.horizontal_stretch(1)
    label = CenteredLabel("Stable", style_identifier="cards-label")

    container = StableContainerUi(cards_container, label, QHBoxLayout())

    return container


class StableUi:
    stable: Stable

    expanded_view: ContainerWidget
    compact_view: ContainerWidget
    turn_view: ContainerWidget

    def __init__(self, stable: Stable):
        self.stable = stable

        self.expanded_view = _create_expanded_view(stable)
        self.compact_view = _create_compact_view(stable)
        self.turn_view = _create_turn_view(stable)
