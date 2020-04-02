#!/usr/bin/python3
"""Accepts an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument. Avoiding SQL injection."""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name = %s
                ORDER BY id ASC""",
                (sys.argv[4],))
    result = cur.fetchall()
    for entry in result:
        print(entry)
    cur.close()
    db.close()
