#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cu = db.cursor()
cu.execute("SELECT * FROM states ORDER BY id")
query_rows = cu.fetchall()
for row in query_rows:
    print(row)
cu.close()
db.close()
