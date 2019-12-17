#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
cu = db.cursor()
cu.execute("""SELECT cities.id, cities.name, states.name
              FROM cities INNER JOIN states ON cities.state_id = states.id
              ORDER BY cities.id""")
query_rows = cu.fetchall()
for row in query_rows:
    print(row)
cu.close()
db.close()
