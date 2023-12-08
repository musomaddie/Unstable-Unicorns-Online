# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
""" game runner """
from dataclasses import dataclass

from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.nursery import Nursery
from game_details.player import AllPlayers
from game_details.utilities import TurnActionType

N_STARTING_CARDS = 4


@dataclass
class Game:
    """ Game object. """
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    players: AllPlayers

    def take_turn(self):
        """ Handles the overall turn action. """
        # TODO -> move most of the player specific interactions into the player class.
        self.players.current_player().take_beginning_of_turn_action()

        self.players.current_player().draw_card(self.deck)

        if self.players.current_player().choose_play_card_or_draw() == TurnActionType.DRAW_CARD:
            self.players.current_player().draw_card(self.deck)
        else:
            print("Playing card")

        self.players.current_player().discard_to_hand_limit(self.discard_pile)
