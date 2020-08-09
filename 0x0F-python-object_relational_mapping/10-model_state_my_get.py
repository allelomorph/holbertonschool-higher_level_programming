#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 10. Get a state
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 5:
        sys.exit('Use: 10-model_state_my_get.py <mysql username> '
                 '<mysql password> <database name> '
                 '<state name to search>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print(state.id)
    else:
        print('Not found')
    session.close()
