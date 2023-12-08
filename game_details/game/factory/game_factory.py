""" factory for creating Game instances. """
from game_details.card.factory import card_factory
from game_details.deck.factory import deck_factory
from game_details.discard_pile.factory import discard_pile_factory
from game_details.game import Game
from game_details.hand.factory import hand_factory
from game_details.nursery.factory import nursery_factory
from game_details.player.factory import player_factory, all_players_factory
from game_details.stable.factory import stable_factory
from play_deciders import DeciderFactory

N_STARTING_CARDS = 4


def create(players: list[str], decider_factory: DeciderFactory) -> Game:
    """ Creates a game instance from the given players and decider. """
    # TODO - allow filtering based on choice of deck.
    deck = deck_factory.create(card_factory.create_all())
    nursery = nursery_factory.create_default()

    # TODO -> improve this -> either create initially empty hands or use a builder (of some kind).
    cards_for_hands = [[] for _ in range(len(players))]
    for _ in range(N_STARTING_CARDS):
        for hand in cards_for_hands:
            hand.append(deck.draw_top())

    hands = [hand_factory.create(hand, decider_factory) for hand in cards_for_hands]
    player_list = [
        player_factory.create(name, hand, stable_factory.create(nursery.get_baby()))
        for name, hand in zip(players, hands)]

    return Game(
        deck,
        discard_pile_factory.create_default(),
        nursery,
        all_players_factory.create(player_list)
    )
