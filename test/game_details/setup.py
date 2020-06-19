from game_details.Card import Card
import sqlite3
import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("tests/game_details")])

DB_NAME = "db/UnstableUnicorns.db"


def find_card_in_db(card_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(f"""SELECT *
                    FROM card_details
                    WHERE name = '{card_name}';
                """)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return Card(result)
