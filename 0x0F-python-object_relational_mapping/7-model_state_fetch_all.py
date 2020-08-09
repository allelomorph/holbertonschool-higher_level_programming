#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 7. All states via SQLAlchemy
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        sys.exit('Use: 7-model_state_fetch_all.py <mysql username> '
                 '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
