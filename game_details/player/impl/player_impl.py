""" player impl. """
from game_details.deck import Deck
from game_details.discard_pile import DiscardPile
from game_details.player import Player
from game_details.utilities import TurnActionType


class PlayerImpl(Player):
    """ Implementation of the player class. """

    def take_beginning_of_turn_action(self) -> None:
        pass

    def draw_card(self, deck: Deck) -> None:
        self.hand.add_card(deck.draw_top())

    def discard_to_hand_limit(self, discard_pile: DiscardPile) -> None:
        while self.hand.must_discard_to_limit():
            discard_pile.add_top(self.hand.choose_card_to_discard())

    @staticmethod
    def choose_play_card_or_draw() -> TurnActionType:
        # TODO - allow playing a card action.
        return TurnActionType.DRAW_CARD

    def take_turn(self, deck: Deck, discard_pile: DiscardPile):
        self.take_beginning_of_turn_action()
        self.draw_card(deck)

        if self.choose_play_card_or_draw() == TurnActionType.DRAW_CARD:
            self.draw_card(deck)
        else:
            print("Playing card")

        self.discard_to_hand_limit(discard_pile)
