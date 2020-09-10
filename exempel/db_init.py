import sqlite3

EXAMPLE_DATASET = (
    ("Alice", "Smith"),
    ("Bob", "Smith"),
    ("Carol", "Brown"),
    ("Carlos", "Rojas"),
    ("Charlie", "Miller")
)

CREATE_TABLE = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

INSERT_DATA = '''
            INSERT INTO person(
                firstname,
                lastname
            )
            VALUES (?, ?)
            '''


def open_connection(filename):
    return sqlite3.connect(filename)


def create_table(connection):
    try:
        connection.execute(CREATE_TABLE)
    except Exception:
        print('Failed to create table')
        raise


def insert_data(connection):
    try:
        with connection:
            connection.executemany(INSERT_DATA, EXAMPLE_DATASET)
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")
    except Exception:
        print("Failed to insert")
        raise
