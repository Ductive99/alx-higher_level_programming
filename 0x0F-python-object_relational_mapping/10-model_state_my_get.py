#!/usr/bin/python3
"""
Script that lists the  state object
that matches the passed name
from a database
"""


def main():
    """
    Connecting to the database and querying it
    """
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).filter(State.name == argv[4]).first()

    if first is None:
        print("Not found")
    else:
        print("{0}".format(first.id))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
