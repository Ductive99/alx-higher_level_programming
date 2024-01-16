#!/usr/bin/python3
"""
Prints all City objects from the hbtn_0e_14_usa DB
"""


def main():
    """
    Connecting to the DB and querying it
    """
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import create_engine
    from model_city import City
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    result = session.query(City, State).filter(State.id == City.state_id)\
                    .order_by(City.id)

    for state, city in result:
        print("{2}: ({1}) {0}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    """ Main Entry Point """
    main()
