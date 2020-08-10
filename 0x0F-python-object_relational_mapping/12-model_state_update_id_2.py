#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 12. Update a state
"""

if __name__ == '__main__':
    from sys import argv, exit
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        exit('Use: 12-model_state_update_id_2.py <mysql username> '
             '<mysql password> <database name> ')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)  # creates decprecated warning

    state_2 = session.query(State).filter_by(id=2).first()
    if state_2 is not None:
        state_2.name = 'New Mexico'
    session.commit()
    session.close()
