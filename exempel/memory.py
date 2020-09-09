import sqlite3

connection = sqlite3.connect(":memory:", isolation_level=None)
cursor = connection.cursor()
cursor.execute("""
                CREATE TABLE person(
                id INTEGER PRIMARY KEY,
                firstname,
                lastname
              )""")

cursor.execute("""INSERT INTO person(
                id,
                firstname,
                lastname
                ) VALUES (
                    1,
                    'john',
                    'smith'
                )""")

cursor.execute("""INSERT INTO person(
                id,
                firstname,
                lastname
                ) VALUES (
                    2,
                    'admin',
                    'smith'
                )""")

cursor.execute("SELECT * FROM person")
for person in cursor:
    print(person)

cursor.connection.close()
