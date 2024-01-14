#!/usr/bin/python3
"""
Script that takes the name of a state as an argument,
and lists all cities of that states in the database.
"""


def main():
    """
    Connecting and querying the database
    """
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (argv[4],))
    results = cursor.fetchall()

    print(", ".join([row[0] for row in results]))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
