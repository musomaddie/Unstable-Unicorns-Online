# TODO - write this class to handle the beginning and end of games. Shouldn't need to do much else besides setup all
#  info and move to next turns (repeatedly).
""" game runner """
from __future__ import annotations

import json
from dataclasses import dataclass

import unstable_unicorns_game.utilities.logger_keys as LK
from unstable_unicorns_game.game.cards.card import Card
from unstable_unicorns_game.game.cards.deck import Deck
from unstable_unicorns_game.game.cards.discard_pile import DiscardPile
from unstable_unicorns_game.game.cards.hand import Hand
from unstable_unicorns_game.game.cards.nursery import Nursery
from unstable_unicorns_game.game.player.all_players import AllPlayers
from unstable_unicorns_game.game.player.player import Player
from unstable_unicorns_game.game.player.stable import Stable
from unstable_unicorns_game.play_deciders.play_decider import PlayDecider
from unstable_unicorns_game.utilities.logger import Logger

N_STARTING_CARDS = 4


def load_all_cards() -> list[Card]:
    """ Creates card objects for every card listed in the json file. """
    file_contents = json.load(open("unstable_unicorns_game/data/card_details.json"))
    # TODO - temporary for testing, delete this later!!
    cards = [Card.create(card_info) for card_info in file_contents]
    while len(cards) < 30:
        cards.append(cards[0])

    return cards


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
        deck = Deck.create(load_all_cards())
        nursery = Nursery.create_default()

        # TODO -> improve this -> either create initially empty hands or use a builder (of some kind).
        cards_for_hands = [[] for _ in range(len(players))]
        for _ in range(N_STARTING_CARDS):
            for hand in cards_for_hands:
                hand.append(deck.draw_top())

        hands = [Hand.create(hand, decider) for hand in cards_for_hands]
        player_list = [
            Player.create(element[0], element[1], Stable.create(nursery.get_baby()), index)
            for index, element in enumerate(zip(players, hands))]

        return cls(deck, DiscardPile.create_default(), nursery, AllPlayers.create(player_list))

    def log_start(self) -> Logger:
        """ Creates a log for the game start. """
        return Logger({
            LK.START_INFO: Logger({
                LK.GAME_CONFIG: self.players.create_log(),
                LK.PLAYER_DETS: [{
                    player.id: player.create_log() for player in self.players
                }]
            })
        })

    def debug_str(self) -> str:
        """ Returns a string (possibly multi-line) describing the current state of the game."""
        # TODO -> consider adding a variable for 'start' for additional config.
        return "\n".join([
            "Created game with:",
            f"\t{self.deck.debug_str()}",
            f"\t{self.nursery.debug_str()}",
            "",
            self.players.debug_str(indents=1)
        ])

    def take_turn(self):
        """ Handles the overall turn action. """
        self.players.current_player().take_turn(self.deck, self.discard_pile)
        self.players.next_player()
