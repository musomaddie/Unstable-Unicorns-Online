# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
""" game runner """
from dataclasses import dataclass

from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.nursery import Nursery
from game_details.player import AllPlayers

N_STARTING_CARDS = 4


@dataclass
class Game:
    """ Game object. """
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    players: AllPlayers
