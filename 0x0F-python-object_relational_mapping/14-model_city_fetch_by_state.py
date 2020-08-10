#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 14. Cities in state
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    if len(argv) != 4:
        exit('Use: 14-model_city_fetch_by_state.py <mysql username> '
             '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)  # creates decprecated warning 1681

    result = session.query(State.name, City.id, City.name).filter(
        City.state_id == State.id).order_by(City.id).all()
    for row in result:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))

    session.close()
    """
    equivalent to:
    SELECT states.name, cities.id, cities.name FROM cities
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;

    alternate method:
    result = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for city, state in result:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    """
