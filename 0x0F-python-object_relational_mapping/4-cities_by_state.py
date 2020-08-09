#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 4. Cities by states"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        print('Use: 0-select_states.py <mysql username> <mysql password>'
              ' <database name>')
        sys.exit()

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities '
                'LEFT JOIN states ON cities.state_id = states.id;')
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
