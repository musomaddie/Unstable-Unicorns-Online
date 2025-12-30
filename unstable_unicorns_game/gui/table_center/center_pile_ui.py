from PyQt6.QtWidgets import QVBoxLayout

import unstable_unicorns_game.gui.resources.style as style
from unstable_unicorns_game.game.cards.multiple_cards_holder import MultipleCardsHolder
from unstable_unicorns_game.gui.cards.cards_ui import CardsContainerWithUi, CardsPileView
from unstable_unicorns_game.gui.resources import alignment
from unstable_unicorns_game.gui.resources.measurement import CENTER_CARD_PILE_MARGINS
from unstable_unicorns_game.gui.widgets.container_widget import ContainerWidget
from unstable_unicorns_game.gui.widgets.label import Label


class CenterPileUi:
    cards: MultipleCardsHolder
    cards_container: CardsContainerWithUi
    view: ContainerWidget

    def __init__(self, cards: MultipleCardsHolder, label_text: str):
        self.cards = cards
        self.cards_container = CardsContainerWithUi(
            cards.cards,
            label=Label(label_text, word_wrap=False, alignment=alignment.center()),
            container_view=CardsPileView(cards.cards),
            overall_view=ContainerWidget(
                layout=QVBoxLayout(),
                style_identifier="container",
                styling=style.table_center_pile_wrapper(),
                margins=CENTER_CARD_PILE_MARGINS,
                alignment=alignment.center()
            ),
        )
        self.view = self.cards_container.overall_view

    def update(self):
        self.cards_container.update()
