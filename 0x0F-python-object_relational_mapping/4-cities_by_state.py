#!/usr/bin/python3
"""
Script to list all cities from
the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    """
    Main Entry Point
    """
    main()
