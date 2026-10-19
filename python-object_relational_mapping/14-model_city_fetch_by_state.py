#!/usr/bin/python3
"""Prints all City objects with the name of their state."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    rows = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state_name, city_id, city_name in rows:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
