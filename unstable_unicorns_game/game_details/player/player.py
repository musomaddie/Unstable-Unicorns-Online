""" Player class """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game_details.deck.deck import Deck
from unstable_unicorns_game.game_details.discard_pile.discard_pile import DiscardPile
from unstable_unicorns_game.game_details.game.action_type import TurnActionType
from unstable_unicorns_game.game_details.hand.hand import Hand
from unstable_unicorns_game.game_details.stable import Stable
from unstable_unicorns_game.game_details.stable.factory import stable_factory


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand
    stable: Stable

    @classmethod
    def create(cls, name: str, hand: Hand, stable: Stable) -> Player:
        return cls(name, hand, stable)

    @classmethod
    def create_default(cls, name: str) -> Player:
        """ Creates a player with the given name and otherwise default values. """
        return cls.create(name, Hand.create_default(), stable_factory.create_default())

    def take_beginning_of_turn_action(self) -> None:
        """ Handles the beginning of turn action. """
        # TODO -> implement this.
        pass

    def draw_card(self, deck: Deck) -> None:
        """ Removes the top card from the given deck and adds it to the hand. """
        # TODO -> I think instead of having a verbose printer like this, I could pass the handler and call
        #  handler.handle() in each method, to make it a lot neater.
        # self.verbose_printer.print("Drawing a card ... ")
        # self.verbose_printer.extend_prefix()

        drawn_card = deck.draw_top()
        self.hand.add_card(drawn_card)

        # self.verbose_printer.unextend_prefix()

    def discard_to_hand_limit(self, discard_pile: DiscardPile) -> None:
        """ Handles the process of discarding to the hand limit. """
        while self.hand.must_discard_to_limit():
            discard_pile.add_top(self.hand.choose_card_to_discard())

    @staticmethod
    def choose_play_card_or_draw() -> TurnActionType:
        # TODO - allow playing a card action.
        return TurnActionType.DRAW_CARD

    def take_turn(self, deck: Deck, discard_pile: DiscardPile):
        """ The turn action for this player. """
        # self.verbose_printer.print(f"({self.name})")
        # self.verbose_printer.extend_prefix()

        self.take_beginning_of_turn_action()
        self.draw_card(deck)

        if self.choose_play_card_or_draw() == TurnActionType.DRAW_CARD:
            self.draw_card(deck)
        else:
            print("Playing card")

        self.discard_to_hand_limit(discard_pile)
        # self.verbose_printer.unextend_prefix()
