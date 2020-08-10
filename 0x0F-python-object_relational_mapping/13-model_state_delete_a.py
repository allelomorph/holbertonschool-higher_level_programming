#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 13. Delete states
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        exit('Use: 13-model_state_delete_a.py <mysql username> '
             '<mysql password> <database name> ')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)  # creates decprecated warning 1681

    a_states = session.query(State).filter(State.name.like('%a%')).all()
    for state in a_states:
        session.delete(state)
    session.commit()
    session.close()
