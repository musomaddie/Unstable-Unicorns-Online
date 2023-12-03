import copy

from game_details.discard_pile.factory import discard_pile_factory


def test_constructor(fake_card):
    discard_pile = discard_pile_factory.create([copy.copy(fake_card) for _ in range(3)])
    assert len(discard_pile) == 3
    assert discard_pile[0] == fake_card
