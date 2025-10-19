# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
""" game runner """
from __future__ import annotations

from dataclasses import dataclass

from unstable_unicorns_game.game_details.card.factory import card_factory
from unstable_unicorns_game.game_details.deck.deck import Deck
from unstable_unicorns_game.game_details.discard_pile.discard_pile import DiscardPile
from unstable_unicorns_game.game_details.hand.factory import hand_factory
from unstable_unicorns_game.game_details.nursery import Nursery
from unstable_unicorns_game.game_details.nursery.factory import nursery_factory
from unstable_unicorns_game.game_details.player import AllPlayers
from unstable_unicorns_game.game_details.player.factory import all_players_factory
from unstable_unicorns_game.game_details.player.factory import player_factory
from unstable_unicorns_game.game_details.stable.factory import stable_factory
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider

N_STARTING_CARDS = 4


@dataclass
class Game:
    """ Game object. """
    deck: Deck
    discard_pile: DiscardPile
    nursery: Nursery
    players: AllPlayers

    @classmethod
    def create(cls, players: list[str], decider: PlayDecider) -> Game:
        """ Creates a game instance from the given players and decider. """
        # TODO - allow filtering based on choice of deck.
        # TODO -> replace card_factory here!!
        deck = Deck.create(card_factory.create_all())
        nursery = nursery_factory.create_default()

        # TODO -> improve this -> either create initially empty hands or use a builder (of some kind).
        cards_for_hands = [[] for _ in range(len(players))]
        for _ in range(N_STARTING_CARDS):
            for hand in cards_for_hands:
                hand.append(deck.draw_top())

        hands = [hand_factory.create(hand, decider) for hand in cards_for_hands]
        player_list = [
            player_factory.create(name, hand, stable_factory.create(nursery.get_baby()))
            for name, hand in zip(players, hands)]
        return cls(deck, DiscardPile.create_default(), nursery, all_players_factory.create(player_list))

    def take_turn(self):
        """ Handles the overall turn action. """
        self.players.current_player().take_turn(self.deck, self.discard_pile)
        self.players.next_player()
