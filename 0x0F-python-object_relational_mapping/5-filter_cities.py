#!/usr/bin/python3
"""Lists all cities from the database nbtn_0e_4_usa"""
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
cu = db.cursor()
cu.execute("""SELECT cities.name FROM cities
              INNER JOIN states ON cities.state_id = states.id
              WHERE states.name = %(states_name)s
              ORDER BY cities.id""", {'states_name': sys.argv[4]})
query_rows = cu.fetchall()
for row in range(len(query_rows)):
    if row < len(query_rows) - 1:
        print(query_rows[row][0], end=", ")
    else:
        print(query_rows[row][0])
cu.close()
db.close()
