#!/usr/bin/python3
"""
Module that list all `states` from the database `hbtn_0e_0_usa`
"""
from sys import argv
import MySQLdb


def main():
    """
    Connecting to database and retrieving the state names
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")

    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    main()
