#!/usr/bin/python3
"""
Script that changes the name of a `State` object
from the database `hbtn_0e_6_usa`

Changes the name of the `State` where id = 2
to 'New Mexico'
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

    to_change = session.query(State).filter_by(id=2).first()
    to_change.name = "New Mexico"

    session.commit()


if __name__ == "__main__":
    """
    Main Entry Point
    """
    main()
