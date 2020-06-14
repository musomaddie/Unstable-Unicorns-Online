import sqlite3
import csv

DB_NAME = "UnstableUnicorns.db"
UNICORN_FILE_NAME = "UnicornDetails.tsv"


def _load_all_unicorns():
    unicorns = []
    with open(UNICORN_FILE_NAME, newline='') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        for row in reader:
            unicorns.append(row)
    return unicorns


def populate_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    unicorns = _load_all_unicorns()
    for unicorn in unicorns:
        # Perform string replacement of double quotes
        for key in unicorn:
            unicorn[key] = unicorn[key].replace('"', "'")
        cur.execute(f'''
                    INSERT INTO unicorn_details
                    VALUES (
                        {unicorn['Counter']},
                        "{unicorn["Card Name"]}",
                        "{unicorn["Type"]}",
                        "{unicorn["Text"]}",
                        "{unicorn["Action on Enter Stable"]}",
                        "{unicorn["Beginning of Turn Action"]}",
                        "{unicorn["Discard Action"]}",
                        "{unicorn["In Stable Effect"]}",
                        "{unicorn["Search Deck"]}",
                        "{unicorn["Shuffle Discard Into Deck"]}",
                        "{unicorn["Scarifice"]}",
                        "{unicorn["Return to Hand"]}",
                        "{unicorn["Search Discard"]}",
                        "{unicorn["Protection"]}",
                        "{unicorn["Draw"]}",
                        "{unicorn["Destroy"]}",
                        "{unicorn["Requires Basic Unicorn"]}",
                        "{unicorn["Action on Leave"]}"
                    );
                    ''')
    conn.commit()
    cur.close()
    conn.close()


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
                    discard_action TEXT,
                    in_stable_effect BOOLEAN,
                    search_deck TEXT,
                    shuffle_deck BOOLEAN,
                    shuffle_discard BOOLEAN,
                    sacrifice TEXT,
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
    populate_db()
