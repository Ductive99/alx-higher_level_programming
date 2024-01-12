#!/usr/bin/python3
"""
Script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""
from sys import argv
import MySQLdb


def main():
    """
    Connecting to the database and querying it.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    query = f"SELECT * FROM states WHERE name = '{argv[4]}'"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)


if __name__ == "__main__":
    main()
