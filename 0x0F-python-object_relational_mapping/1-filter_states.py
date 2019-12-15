#!/usr/bin/python3
"""Lists all states with a name starting with N. Database hbtn_0e_0_usa"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cu = db.cursor()
    cu.execute("""SELECT * FROM states
                           WHERE name LIKE BINARY 'N%'
                           ORDER BY states.id;""")
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    db.close()
