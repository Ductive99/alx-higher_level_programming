#!/usr/bin/python3
"""
Script 2-my_filter_states.py
Improved to handle SQL injections
"""


def main():
    """
    function to connect to the database
    and to query  it.
    """
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY %s \
                    ORDER BY states.id ASC", (argv[4],))

    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    """
    Main Entry Point
    """
    main()
