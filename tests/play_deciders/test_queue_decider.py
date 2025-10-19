""" Tests the queue decider. """
import pytest

from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.card_type import CardType
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.play_deciders.queue_decider import QueueDecider


@pytest.fixture
def decider() -> QueueDecider:
    return QueueDecider()


class TestChooseDiscard:
    def test_no_cards(self, decider):
        hand = Hand.create([])
        result = decider.choose_discard(hand)

        assert result is None

    def test_with_cards(self, decider):
        hand = Hand.create([
            Card.create_default("First card!", CardType.BASIC_UNICORN),
            Card.create_default("Second card", CardType.BASIC_UNICORN)
        ])
        result = decider.choose_discard(hand)

        assert result == hand.cards[0]
