import sqlite3

EXAMPLE_DATASET = (
    (1, "Alice", "Smith"),
    (2, "Bob", "Smith"),
    (3, "Carol", "Brown"),
    (4, "Carlos", "Rojas"),
    (5, "Charlie", "Miller")
)

CREATE_TABLE = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
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
        connection.executemany(
            '''
            INSERT OR IGNORE INTO person(
                id,
                firstname,
                lastname
            )
            VALUES (?, ?, ?)
            ''',
            EXAMPLE_DATASET)
    except Exception:
        print("Failed to insert")
        raise
