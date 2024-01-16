#!/usr/bin/python3
"""
Script that deletes all State objects
with a name containing the letter a
from the hbtn_0e_6_usa database
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

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        session.delete(state)

    session.commit()


if __name__ == "__main__":
    """ Main Entry Point """
    main()
