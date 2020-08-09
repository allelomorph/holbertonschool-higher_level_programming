#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 9. Contains `a`
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        sys.exit('Use: 9-model_state_filter_a.py <mysql username> '
                 '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    states = session.query(State).order_by(State.id)
    states = states.filter(State.name.like('%a%')).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
