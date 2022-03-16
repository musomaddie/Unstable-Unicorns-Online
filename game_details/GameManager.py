import sqlite3
import os
import sys
import random

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("game_details")])

from game_details.Card import Card
from game_details.Card import CardType
from game_details.DeckManager import DeckManager
from game_details.DiscardManager import DiscardManager
from game_details.NurseryManager import NurseryManager
from game_details.PlayersManager import PlayersManager
from game_details.TurnManager import TurnManager


DB_NAME = "../db/UnstableUnicorns.db"

""" create_new_game: starts the game """
class GameManager:
    """ Responsible for managing the overall state of the game.

    Parameters:
        turn (TurnManager): manages the current turn.
        deck (DeckManager): manages the deck.
        discard_pile (DiscardManager): manages the discard pile
        players (PlayerManager): manages all the players
        nursery (NuseryManager): manages the nursery (baby bois)

    Methods:
        start_game(): starts the gameplay.
    """

    def __init__(self, deck, discard_pile, players, nursery):
        self.deck = deck
        self.discard_pile = discard_pile
        self.players = players
        self.nursery = nursery

    def start_game(self):
        """ Starts the gameplay after a game has been setup. 

        TODO: need a better way of determining who goes first.
        
        Returns:
            winning_player (PlayerManager): the overall wining player!
        """
        i = 0
        while True:
            # Check winner - for all players not just the current one.
            for player in self.players.all_players():
                if player.has_won():
                    return player
            # TODO: Players can win at any point during their turn and the game
            # immediately ends so this is a little tricky.
            TurnManager(self.players.find_player_from_index(i %
                len(self.players.all_players())),
                    self.players, self.deck, self.discard_pile, self.nursery)
            i += 1


def create_game(starting_decks, player_names):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Create the deck
    deck_card_list = []
    for deck in starting_decks:
        cur.execute(f"""SELECT name, card_type, card_description, action_on_enter,
                            action_on_begin, discard_action, in_stable_effect,
                            search_deck, shuffle_deck, shuffle_discard,
                            sacrifice, return_to_hand, search_discard,
                            protection, draw, destroy, requires_basic,
                            action_on_leave
                        FROM unicorn_details JOIN pack_details USING (name)
                        WHERE deck='{deck}';
                    """)
        for result in cur.fetchall():
            processed_result = []
            for i, r in enumerate(result):
                if i == 1:
                    processed_result.append(CardType.create_enum_from_string(r))
                elif i >= 3:
                    processed_result.append(r == True)
                else:
                    processed_result.append(r)
            deck_card_list.append(Card(*result))

    cur.close()
    conn.close()

    random.shuffle(deck_card_list)
    deckManager = DeckManager(deck_card_list)
    discardManager = DiscardManager([])

    # Create the nursery and the players
    nursery = NurseryManager();
    players = PlayersManager(player_names)

    # Give each player a baby unicorn and 5 cards
    players.prepare_game_start(nursery, deckManager)

    # Start the game
    game = GameManager(deckManager, discardManager, players, nursery)
    game.start_game()


if __name__ == "__main__":
    create_game(["Standard", "Rainbow", "Dragon", "NSFW"], 
            ["Alice", "Bob", "Charlie", "Dave"])
