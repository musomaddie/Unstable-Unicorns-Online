import sqlite3

DB_NAME = "UnstableUnicorns.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS unicorn_details""")
    cur.execute("""DROP TABLE IF EXISTS pack_details""")

    cur.execute('''
                CREATE TABLE unicorn_details (
                    counter INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    card_type TEXT,
                    action_on_enter BOOLEAN,
                    action_on_begin BOOLEAN,
                    discard_action BOOLEAN,
                    in_stable_effect BOOLEAN,
                    search_deck TEXT,
                    shuffle_deck BOOLEAN,
                    shuffle_discard BOOLEAN,
                    scarifice TEXT,
                    return_to_hand BOOLEAN,
                    search_discard TEXT,
                    protection TEXT,
                    draw TEXT,
                    destroy TEXT,
                    requires_basic BOOLEAN,
                    action_on_leave BOOLEAN
                );
                ''')

    cur.execute('''
                CREATE TABLE pack_details (
                    name TEXT NOT NULL,
                    quantity INTEGER,
                    deck TEXT NOT NULL,
                    PRIMARY KEY(name, deck),
                    FOREIGN KEY (name) REFERENCES unicorn_details(name)
                );
                ''')

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    init_db()
    # populate_db()
