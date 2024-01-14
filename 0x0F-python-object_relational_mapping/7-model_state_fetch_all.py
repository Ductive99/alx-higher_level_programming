#!/usr/bin/python3
"""
Script that lists all state objects
from a database
"""


def main():
    """
    Connecting to the database and querying it
    """
    from sqlalchemy.orm import sessionmaker
    from sqlqlchemy import create_engine
    from model_state import Base, State
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{0}: {1}".format(instance.id, instance.name))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
