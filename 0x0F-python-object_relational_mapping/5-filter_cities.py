#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities
                 INNER JOIN states
                 ON cities.state_id = states.id
                 WHERE states.name = %s
                 ORDER BY cities.id ASC""", (sys.argv[4],))
    query_rows = cur.fetchall()
    n = len(query_rows)
    for i in range(0, n):
        if i < n - 1:
            print(query_rows[i][0], end=", ")
        else:
            print(query_rows[i][0])
    cur.close()
    conn.close()
