from db_init import open_connection, create_table, insert_data


def select_firstname_equals(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            timestamp
        FROM person
        WHERE
            firstname = ?
        ''', [name]
    ))


def select_firstname_like(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            timestamp
        FROM person
        WHERE
            firstname LIKE ?
        ''', [name]
    ))


def main():
    connection = open_connection("example.db")
    with connection:
        create_table(connection)
        insert_data(connection)
        print(select_firstname_like(connection, "C%"))

    connection.close()


if __name__ == "__main__":
    main()
