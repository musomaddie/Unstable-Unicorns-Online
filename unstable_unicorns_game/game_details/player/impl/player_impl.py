""" player impl. """
from unstable_unicorns_game.game_details.deck import Deck
from unstable_unicorns_game.game_details.discard_pile import DiscardPile
from unstable_unicorns_game.game_details.game.action_type import TurnActionType
from unstable_unicorns_game.game_details.player import Player


class PlayerImpl(Player):
    """ Implementation of the player class. """

    def take_beginning_of_turn_action(self) -> None:
        pass
        # self.verbose_printer.print("Beginning of turn action ...")
        # self.verbose_printer.extend_prefix()
        #
        # # TODO -> implement this.
        # self.verbose_printer.print("No action to take")
        # self.verbose_printer.unextend_prefix()

    def draw_card(self, deck: Deck) -> None:
        # TODO -> I think instead of having a verbose printer like this, I could pass the handler and call
        #  handler.handle() in each method, to make it a lot neater.
        # self.verbose_printer.print("Drawing a card ... ")
        # self.verbose_printer.extend_prefix()

        drawn_card = deck.draw_top()
        self.hand.add_card(drawn_card)

        # self.verbose_printer.unextend_prefix()

    def discard_to_hand_limit(self, discard_pile: DiscardPile) -> None:
        while self.hand.must_discard_to_limit():
            discard_pile.add_top(self.hand.choose_card_to_discard())

    @staticmethod
    def choose_play_card_or_draw() -> TurnActionType:
        # TODO - allow playing a card action.
        return TurnActionType.DRAW_CARD

    def take_turn(self, deck: Deck, discard_pile: DiscardPile):
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
