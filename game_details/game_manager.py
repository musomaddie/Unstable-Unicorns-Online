import sqlite3
import os
import sys
import random
import copy

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.Card import Card
from game_details.Player import Player
# from game_details.CardLocation import CardLocation

DB_NAME = "db/UnstableUnicorns.db"
WIN_NUMBER = 7  # TODO: modify based on number of players


def make_choice(items):
    print(f"The possible items are {items}")
    return int(input("NUM? "))


class GameManager():
    def _init_starting_decks_check(self, starting_decks):
        if len(starting_decks) == 0:
            return False
        if len(starting_decks) == 1 and starting_decks[0] != "Standard":
            return False
        # TODO More sanity checks
        return True

    def _init_populate_deck(self, starting_decks):
        valid_decks = ["Standard", "Rainbow", "Dragon", "Uncut", "NSFW"]

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Select the starting deck cards
        for deck in starting_decks:
            if deck not in valid_decks:
                continue
            cur.execute(f"""SELECT *
                            FROM card_details JOIN pack_details USING (name)
                            WHERE deck='{deck}';
                        """)
            self.deck = [Card(result) for result in cur.fetchall()
                         for _ in range(0, result[-2])
                         if result[2] != "Baby Unicorn"]

            cur.close()
            conn.close()

        random.shuffle(self.deck)

    def _init_populate_nursery(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(""" SELECT *
                        FROM card_details
                        WHERE card_type = 'Baby Unicorn'
                    """)
        baby_unicorn = Card(cur.fetchone())
        self.nursery = [copy.copy(baby_unicorn) for _ in range(25)]
        cur.close()
        conn.close()

    def _init_populate_players(self, player_names):
        self.players = [Player(player, copy.copy(self.nursery[0]))
                        for player in player_names]

    def _init_deal(self):
        [player.add_to_hand(self.deck.pop(0))
         for _ in range(5) for player in self.players]

    def __init__(self, starting_decks, player_names):
        # Main Variables
        self.deck = []
        self.discard_pile = []
        self.players = []
        self.nursery = []

        # Other variables to assist with turn management
        self.current_player = None
        self.played_card = None
        # This card is what all methods will actually use. (not played)
        self.selected_card = None
        # Same with player
        self.selected_player = None

        # A dictionary of additional information used only for one method
        self.additional_info = {}

        # Set up the starting game variables
        if not self._init_starting_decks_check(starting_decks):
            print("No valid decks")
            return

        self._init_populate_deck(starting_decks)
        self._init_populate_nursery()
        self._init_populate_players(player_names)
        self._init_deal()

    # #########################################################################
    #                        END OF SET UP SECTION                            #
    # #########################################################################

    def move_next_state(card, next_states):
        if not card:
            return False
        if card.in_dict(next_states):
            return next_states[card.name]()

    def _activate_magic_card(self):
        """ Handles activating the given magic card.

            Requires:
                selected_card
        """
        pass

    def _add_to_stable(self):
        """ Handles adding the selected card to the stable.

            Requires:
                selected player
                selected card
        """

    def _beginning_turn_action(self):
        """ Handles the beginning of the current turn action

            Requires:
                current_player
        """
        pass

    def _card_play(self):
        """ Handles the playing of the current card.

            Requires:
                current_player
                played_card
        """
        self.selected_card = self.played_card
        self.selected_player = self.current_player

        if self.played_card.is_magic_type():
            self._activate_magic_card()
            return
        if self.played_card.is_unicorn():
            self._add_to_stable()
            return
        self.additional_info["not_yourself"] = False
        self._choose_player()
        self._add_to_stable()

    def _choose_player(self):
        """ Handles choosing a player. The choice is made by the current
        player.

            Requires:
                current_player
                not_yourself (additional_info)
        """
        chosen_player = self.players[make_choice(self.players)]
        self.selected_player = chosen_player

    def _draw(self):
        """ Handles the draw action

            Requires:
                current_player
        """
        self.current_player.add_to_hand(self.deck.pop(0))

    def player_turn(self, current_player):
        # TODO: should this be in the player object??
        self.current_player = current_player

        # Check for beginning of turn action
        self._beginning_turn_action()

        # Draw Card
        self._draw()

        # Action phase
        # TODO: handle a second drawn card
        selected_card = 0
        self.played_card = self.current_player.hand[selected_card]
        self._card_play()

        # End of Turn phase
        # TODO ^^

        # Check Win Condition: (must also do throughout)
        return True

    def play_game(self):
        counter = 0
        while True:
            if self.player_turn(self.players[counter & len(self.players)]):
                break
        counter += 1


if __name__ == '__main__':
    print("HELLO WORLD")
    game = GameManager(["Standard"], ["Alice", "Bob"])
