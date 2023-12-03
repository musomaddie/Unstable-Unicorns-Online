""" Tests the queue decider. """
from game_details.card import CardType
from game_details.card.factory import card_factory
from game_details.hand import Hand
from game_details.player import Player
from game_details.stable import Stable
from play_deciders import QueueDecider


def test_decide_discard():
    player = Player(
        name="Aelin",
        hand=Hand([
            card_factory.create_default("First card!", CardType.BASIC_UNICORN),
            card_factory.create_default("Second card", CardType.BASIC_UNICORN)]),
        stable=Stable.create_default()
    )
    queue_decider = QueueDecider(player)

    assert queue_decider.decide_discard() == player.hand.cards[0]
