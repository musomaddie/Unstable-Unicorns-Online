""" Factory for creating MultipleCardsHolder instances. """
from unstable_unicorns_game.game_details.card import MultipleCardsHolder, Card


def create_default() -> MultipleCardsHolder:
    """ Creates a MultipleCardsHolder with no contents. """
    return MultipleCardsHolder(cards=[])


def create(card: Card) -> MultipleCardsHolder:
    """ Creates a Multiple cardholder with the given card."""
    return MultipleCardsHolder(cards=[card])
