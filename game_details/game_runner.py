# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
""" game runner """
from dataclasses import dataclass

from game_details.card.factory import card_factory
from game_details.deck import Deck
from game_details.deck.factory import deck_factory
from game_details.discard_pile import DiscardPile
from game_details.discard_pile.factory import discard_pile_factory
from game_details.hand import Hand
from game_details.nursery import Nursery
from game_details.player import AllPlayers, Player
from game_details.stable import Stable
from play_deciders import DeciderFactory

N_STARTING_CARDS = 4


@dataclass
class Game:
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    players: AllPlayers

    @staticmethod
    def create_game(players: list[str], decider_factory: DeciderFactory):
        """ Creates a brand-new game

        :param players: a list of player names
        :param decider_factory: the decider factory which creates a decider to use.
        :return: the created game
        """
        # TODO - allow filtering based on choice of deck.
        deck = deck_factory.create(card_factory.create_all())
        nursery = Nursery.create_default()

        # Before creating player objects we need to create the hand objects for them.
        hands = [Hand.create_default() for _ in range(len(players))]
        for _ in range(N_STARTING_CARDS):
            for hand in hands:
                hand.add_card(deck.draw_top())
        all_players = []

        for player_name, hand in zip(players, hands):
            all_players.append(
                Player.create(player_name, hand, Stable.create(nursery.get_baby()), decider_factory))

        return Game(
            deck,
            discard_pile_factory.create_default(),
            nursery,
            AllPlayers(all_players)
        )
