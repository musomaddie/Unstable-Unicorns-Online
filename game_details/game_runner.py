# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
from dataclasses import dataclass

from game_details.card import Card
from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.hand import Hand
from game_details.nursery import Nursery
from game_details.player import AllPlayers, Player
from game_details.stable import Stable

N_STARTING_CARDS = 4


@dataclass
class Game:
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    players: AllPlayers

    @staticmethod
    def create_game(players: list[str]):
        # TODO - allow filtering based on choice of deck.
        deck = Deck(Card.create_all_cards())
        nursery = Nursery()

        # Before creating player objects we need to create the hand objects for them.
        hands = [Hand() for _ in range(len(players))]
        for i in range(N_STARTING_CARDS):
            for hand in hands:
                hand.add_card(deck.draw_top())
        all_players = []

        for player_name, hand in zip(players, hands):
            all_players.append(
                Player(player_name, hand, Stable(nursery.get_baby()))
            )

        return Game(
            deck,
            DiscardPile(),
            nursery,
            AllPlayers(all_players)
        )
