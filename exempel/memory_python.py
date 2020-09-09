import sqlite3

# Source [https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions]

con = sqlite3.connect(":memory:")
con.execute(
    """CREATE TABLE person(
        id INTEGER PRIMARY KEY,
        firstname VARCHAR UNIQUE
    )""")

# Successful, con.commit() is called automatically afterwards
with con:
    con.execute(
        """INSERT INTO person(
            firstname
            ) VALUES (?)
        """,
        ("Joe",))

# con.rollback() is called after the with block finishes with an exception, the
# exception is still raised and must be caught
try:
    with con:
        con.execute(
            """INSERT INTO person(
                firstname
                ) VALUES (?)
            """,
            ("Joe",))
except sqlite3.IntegrityError:
    print("couldn't add Joe twice")

# Connection object used as context manager only commits
# or rollbacks transactions, so the connection object should be closed manually
con.close()
