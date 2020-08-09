#!/usr/bin/python3
"""0x0F. Python - Object-relational mapping - task 1. Filter states"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 5:
        sys.exit('Use: 1-filter_states.py <mysql username> <mysql password>'
                 ' <database name> <state name searched>')

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT name FROM states")
    state_names = cur.fetchall()
    if sys.argv[4] in state_names:
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY '" +
                    sys.argv[4] + "' ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    cur.close()
    conn.close()
