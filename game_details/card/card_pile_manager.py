from dataclass import dataclass

from game_details.card.card import Card


@dataclass
class CardPileManager:
    """ A super class for managing anything that is a pile of cards (e.g. deck, discard pile). """

    cards: list[Card]
