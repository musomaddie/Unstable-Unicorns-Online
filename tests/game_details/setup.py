import os
import random
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.Card import Card
from game_details.DeckManager import DeckManager

DB_NAME = "../../db/UnstableUnicorns.db"

def find_card_in_db(card_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(f"""SELECT name, card_type, card_description, action_on_enter,
                        action_on_begin, discard_action, in_stable_effect,
                        search_deck, shuffle_deck, shuffle_discard,
                        sacrifice, return_to_hand, search_discard,
                        protection, draw, destroy, requires_basic,
                        action_on_leave
                    FROM unicorn_details
                    WHERE name=?""", (card_name,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return Card(*result)

def random_selection_from_db(number):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(f"""SELECT name, card_type, card_description, action_on_enter,
                        action_on_begin, discard_action, in_stable_effect,
                        search_deck, shuffle_deck, shuffle_discard,
                        sacrifice, return_to_hand, search_discard,
                        protection, draw, destroy, requires_basic,
                        action_on_leave
                    FROM unicorn_details;
                """)
    all_cards = []
    for result in cur.fetchall():
        processed_result = []
        for i, r in enumerate(result):
            if i >= 3:
                processed_result.append(r == True)
            else:
                processed_result.append(r)
        all_cards.append(Card(*result))
    random.shuffle(all_cards)
    return DeckManager(all_cards[:number])
