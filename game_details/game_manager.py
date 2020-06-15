import sqlite3
import os
import sys
import random

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("game_details")])
from game_details.Card import Card

DB_NAME = "db/UnstableUnicorns.db"
DECK = []
DISCARD_PILE = []
PLAYERS = []


def create_game(starting_decks):
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
            for _ in range(0, result[-2])]

    random.shuffle(DECK)

    cur.close()
    conn.close()


if __name__ == '__main__':
    create_game(["Standard", "Dragon"])
