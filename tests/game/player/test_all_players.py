""" Tests for all players """

from _pytest.fixtures import fixture

from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player


@fixture
def all_players() -> AllPlayers:
    """ Creates an AllPlayers object containing 3 players - Alice, Bob and Charlie."""
    return AllPlayers.create(
        [Player.create_default(name) for name in ["Alice", "Bob", "Charlie"]]
    )


def test_len(all_players):
    assert len(all_players) == 3


def test_iterator(all_players):
    expected_names = ["Alice", "Bob", "Charlie"]
    for actual, expect in zip(all_players, expected_names):
        assert actual.name == expect


def test_current_player():
    pass
