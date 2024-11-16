""" Tests the queue decider. """
from unstable_unicorns_game.game_details.card import CardType
from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.player.factory import player_factory
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.play_deciders import decider_factory
from unstable_unicorns_game.play_deciders.queue_decider import QueueDiscardDecider


def test_decide_discard():
    player = player_factory.create(
        name="Aelin",
        hand=hand_factory.create([
            card_factory.create_default("First card!", CardType.BASIC_UNICORN),
            card_factory.create_default("Second card", CardType.BASIC_UNICORN)],
            decider=decider_factory.create("queue")
        ),
        stable=stable_factory.create_default(),
    )
    queue_decider = QueueDiscardDecider(player.hand)

    assert queue_decider.decide() == player.hand.cards[0]
