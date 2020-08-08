#!/usr/bin/python3
"""0x0F. Python - ORM - task 2. Filter states by user input"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '" + sys.argv[4] +
                "' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()