import copy

from game_details.deck import Deck


def test_constructor(fake_card):
    deck = Deck([copy.copy(fake_card) for _ in range(3)])
    assert len(deck) == 3
    assert deck[0] == fake_card
