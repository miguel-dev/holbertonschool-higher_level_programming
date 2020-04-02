#!/usr/bin/python3
"""Accepts an argument and displays all values
in the states table of hbtn_0e_0_usa where name
matches the argument"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    sql_query = '''SELECT * FROM states
                 WHERE name = "{:s}"
                 COLLATE latin1_general_cs
                 ORDER BY id ASC'''.format(sys.argv[4])
    cur.execute(sql_query)
    result = cur.fetchall()
    if result:
        for entry in result:
            print(entry)
    cur.close()
    db.close()
