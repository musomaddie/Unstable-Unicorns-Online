from dataclass import dataclass

from game_details.card import Card


@dataclass
class CardPile:
    """ A super class for managing anything that is a pile of cards (e.g. deck, discard pile). """

    cards: list[Card]
