""" Tests the queue decider. """
from unstable_unicorns_game.game_details.card.card import Card
from unstable_unicorns_game.game_details.card.card_type import CardType
from unstable_unicorns_game.game_details.hand.hand import Hand
from unstable_unicorns_game.game_details.player.player import Player
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.play_deciders.factory import decider_factory
from unstable_unicorns_game.play_deciders.impl.queue_decider import QueueDiscardDecider


def test_decide_discard():
    player = Player.create(
        name="Aelin",
        hand=Hand.create([
            Card.create_default("First card!", CardType.BASIC_UNICORN),
            Card.create_default("Second card", CardType.BASIC_UNICORN)
        ],
            decider=decider_factory.create("queue")
        ),
        stable=stable_factory.create_default(),
    )
    queue_decider = QueueDiscardDecider(player.hand)

    assert queue_decider.decide() == player.hand.cards[0]
