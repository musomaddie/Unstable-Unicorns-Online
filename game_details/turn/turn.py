from dataclasses import dataclass

from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.nursery import Nursery
from game_details.player import Player, AllPlayers
from game_details.utilities import ActionType


@dataclass
class Turn:
    """ A class for all turn related objects.

    A turn has 4 phases:
        (1) Beginning of turn: any beginning of turn actions
        (2) Draw: Draw one card from the draw pile
        (3) Action: either draw again or play a card
        (4) End: discard down to the hand limit (default 7).
    """
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    current_player: Player
    all_players_manager: AllPlayers

    def take_turn(self):
        """ Handles the overall turn action. """
        self.current_player.take_beginning_of_turn_action()

        self.current_player.draw_card(self.deck)

        if self.current_player.choose_play_card_or_draw() == ActionType.DRAW_CARD:
            self.current_player.draw_card(self.deck)
        else:
            print("Playing card")

        self.current_player.discard_to_hand_limit(self.discard_pile)
