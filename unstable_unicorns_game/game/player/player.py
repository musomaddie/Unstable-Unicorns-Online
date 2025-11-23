""" Player class """
from __future__ import annotations

from dataclasses import dataclass

import unstable_unicorns_game.utilities.logger_keys as LK
from unstable_unicorns_game.game.actions.action_type import TurnActionType
from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.utilities.logger import Logger


@dataclass
class Player:
    """ A dataclass for all attributes related to the player. """
    name: str
    hand: Hand
    stable: Stable
    id: str = ""

    @classmethod
    def create(cls, name: str, hand: Hand, stable: Stable, id_int: int = 0) -> Player:
        return cls(name, hand, stable, f"{name}_{id_int}")

    @classmethod
    def create_default(cls, name: str) -> Player:
        """ Creates a player with the given name and otherwise default values. """
        return cls.create(name, Hand.create_default(), Stable.create_default())

    def create_log(self) -> Logger:
        """ Creates a dictionary of log information for this player. """
        return Logger(
            {
                LK.HAND: self.hand.log_all(),
                LK.STABLE: self.stable.log()
            })

    def debug_str(self, indents: int = 0, include_id=False) -> str:
        """ Returns a string (possibly multi-line) describing the current state of the player."""
        return "\n".join(
            [
                '\t' * indents + f"{self.name}{f' ({self.id})' if include_id else ''}:",
                self.hand.debug_str(indents=indents + 1),
                self.stable.debug_str(indents=indents + 1),
                ""]
        )

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
            discard_pile.add_top(self.hand.discard())

    @staticmethod
    def choose_play_card_or_draw() -> TurnActionType:
        # TODO - allow playing a card action. AND make non static ???
        return TurnActionType.DRAW_CARD

    def take_turn(self, deck: Deck, discard_pile: DiscardPile):
        """ The turn action for this player. """

        self.take_beginning_of_turn_action()
        self.draw_card(deck)

        if self.choose_play_card_or_draw() == TurnActionType.DRAW_CARD:
            self.draw_card(deck)
        else:
            print("Playing card")

        self.discard_to_hand_limit(discard_pile)

    def play_card(self, card: Card):
        # TODO -> DOCUMENTATION.
        # TODO -> implement this fully, to keep things simple for wiring purposes let's just remove the card from the
        #  hand, and print out its info.
        self.hand.remove(card)

        print(f"PLAYING {card.unique_id}")
