#!/usr/bin/python3
"""
Script that lists the first state object
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

    first = session.query(State).order_by(State.id).first()

    if first is None:
        print("Nothing")
    else:
        print("{0}: {1}".format(first.id, first.name))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
