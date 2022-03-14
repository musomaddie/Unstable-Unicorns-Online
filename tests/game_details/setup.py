import sqlite3
import os
import sys
import copy

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))[
    0:-len("tests/game_details")])

from game_details.Card import Card

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
