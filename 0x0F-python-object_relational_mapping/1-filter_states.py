#!/usr/bin/python3
"""
Module that list all states with a name starting with 'N'
from the hbtn_0e_0_usa database
"""
from sys import argv
import MySQLdb


def main():
    """
    Connecting to the DB and querying it
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    """Main Entry"""
    main()
