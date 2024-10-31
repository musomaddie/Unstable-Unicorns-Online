import pytest

from game_details.card import CardType
from game_details.card.factory import card_factory
from game_details.stable import Stable
from game_details.stable.factory import stable_factory


@pytest.fixture
def stable() -> Stable:
    """ Returns a stable for testing. """
    return stable_factory.create(
        card_factory.create_default("bubba", CardType.BABY_UNICORN))


def test_create(stable):
    assert len(stable.unicorns) == 1
    assert stable.unicorns[0].card_type == CardType.BABY_UNICORN

    assert len(stable.upgrades) == 0
    assert len(stable.downgrades) == 0
