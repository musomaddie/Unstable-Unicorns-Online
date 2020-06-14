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


def create_game():
    # TODO: choose number players
    # TODO: choose the decks to play with

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM card_details JOIN pack_details USING (name);")
    [DECK.append(Card(result)) for result in cur.fetchall()
     for _ in range(0, result[-2])]
    random.shuffle(DECK)

    cur.close()
    conn.close()


if __name__ == '__main__':
    create_game()
    print(DECK)
