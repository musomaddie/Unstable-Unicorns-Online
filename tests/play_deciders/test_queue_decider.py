""" Tests the queue decider. """
from game_details.card import CardType
from game_details.card.factory import card_factory
from game_details.hand.factory import hand_factory
from game_details.player.factory import player_factory
from game_details.stable.factory import stable_factory
from play_deciders import QueueDiscardDecider, DeciderType, DeciderFactory


def test_decide_discard():
    player = player_factory.create(
        name="Aelin",
        hand=hand_factory.create([
            card_factory.create_default("First card!", CardType.BASIC_UNICORN),
            card_factory.create_default("Second card", CardType.BASIC_UNICORN)],
            decider_factory=DeciderFactory(DeciderType.QUEUE)
        ),
        stable=stable_factory.create_default(),
    )
    queue_decider = QueueDiscardDecider(player.hand)

    assert queue_decider.decide_discard() == player.hand.cards[0]
