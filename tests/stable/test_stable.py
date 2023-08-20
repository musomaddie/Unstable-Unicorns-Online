import pytest

from game_details.card import Card, CardType
from game_details.stable import Stable


@pytest.fixture
def stable():
    return Stable.create_stable(
        Card("bubba", CardType.BABY_UNICORN, "I'm just a baby")
    )


def test_create(stable):
    assert len(stable.unicorns) == 1
    assert stable.unicorns[0].card_type == CardType.BABY_UNICORN

    assert len(stable.upgrades) == 0
    assert len(stable.downgrades) == 0
