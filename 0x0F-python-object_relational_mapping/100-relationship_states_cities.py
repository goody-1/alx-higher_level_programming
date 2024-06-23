#!/usr/bin/python3
"""Script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California" if it doesn't exist
    california = session.query(State).filter_by(name='California').first()
    if not california:
        california = State(name='California')
        session.add(california)
        session.commit()

    # Create the City "San Francisco" and associate it with the State
    # "California"
    san_francisco = City(name='San Francisco', state=california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
