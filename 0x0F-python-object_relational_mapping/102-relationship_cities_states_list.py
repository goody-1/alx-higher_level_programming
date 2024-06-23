#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_by_states = session.query(
        func.row_number().over(order_by=City.id).label('row_id'),
        City.name,
        State.name
    ).join(State).order_by(City.id.asc()).all()

    for city in cities_by_states:
        row_id, city_name, state_name = city
        print(f"{row_id}: {city_name} -> {state_name}")

    # Close the session
    session.close()
