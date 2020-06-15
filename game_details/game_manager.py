import sqlite3
import os
import sys
import random

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.Card import Card
from game_details.Player import Player

DB_NAME = "db/UnstableUnicorns.db"
DECK = []
DISCARD_PILE = []
PLAYERS = []


def _handle_beginning_turn_action(current_player):
    pass


def _handle_draw(current_player):
    pass


def _handle_card_play(current_player, card):
    pass


def _handle_end_turn(current_player):
    pass


# Manages the turn: will return True if winning condition is met
def player_turn(current_player):
    print(f"It is {current_player}")

    # Beginning of Turn Action
    _handle_beginning_turn_action(current_player)

    # Draw card
    _handle_draw(current_player)

    # Action phase
    # action = input("Action? ")
    action = 0
    if action == "draw":
        _handle_draw(current_player)
    else:  # Assuming typed card correctly (will number)
        _handle_card_play(current_player, current_player.play_card(action))

    # End of turn action
    _handle_end_turn(current_player)

    # Check for winning condition

    return True


def play_game():
    counter = 0
    while True:
        if player_turn(PLAYERS[counter % len(PLAYERS)]):
            break
        counter += 1


def create_game(starting_decks, player_names):
    DECK.clear()
    DISCARD_PILE.clear()
    PLAYERS.clear()
    valid_decks = ["Standard", "Rainbow", "Dragon", "Uncut", "NSFW"]

    if len(starting_decks) == 0:
        return
    if len(starting_decks) == 1 and starting_decks[0] != "Standard":
        # TODO: maybe edge case where all nonsense decks but one which isn't
        # standard
        return

    if len(player_names) <= 2:  # TODO: add in more rules for less players
        return

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for deck in starting_decks:
        if deck not in valid_decks:
            continue
        cur.execute(f"""SELECT *
                        FROM card_details JOIN pack_details USING (name)
                        WHERE deck='{deck}';
                    """)
        [DECK.append(Card(result)) for result in cur.fetchall()
            for _ in range(0, result[-2]) if result[2] != "Baby Unicorn"]
    cur.execute("""SELECT *
                    FROM card_details
                    WHERE card_type = 'Baby Unicorn'
                """)
    baby_unicorn = Card(cur.fetchone())
    random.shuffle(DECK)

    cur.close()
    conn.close()

    for player in player_names:
        PLAYERS.append(Player(player, baby_unicorn))  # SAME CARD FOR ALL

    # Deal cards out
    for i in range(5):
        for player in PLAYERS:
            player.add_card(DECK.pop(0))


if __name__ == '__main__':
    create_game(["Standard", "Dragon", "Rainbow", "NSFW", "Uncut"],
                ["Alice", "Bob", "Charlie"])
    play_game()
