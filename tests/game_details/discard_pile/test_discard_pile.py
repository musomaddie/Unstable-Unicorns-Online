import copy

from game_details.discard_pile import DiscardPile


def test_constructor(fake_card):
    discard_pile = DiscardPile([copy.copy(fake_card) for _ in range(3)])
    assert len(discard_pile) == 3
    assert discard_pile[0] == fake_card
