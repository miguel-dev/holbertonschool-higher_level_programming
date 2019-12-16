#!/usr/bin/python3
"""Takes an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cu = db.cursor()
    cu.execute("""SELECT * FROM states WHERE name = '{}'
                           ORDER BY id;""".format(sys.argv[4]))
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    db.close()
