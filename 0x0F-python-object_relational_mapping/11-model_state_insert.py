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
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")

    session.add(louisiana)
    session.commit()
    print("{0}".format(louisiana.id))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
