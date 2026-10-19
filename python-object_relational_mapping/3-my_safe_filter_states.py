#!/usr/bin/python3
"""Lists all states matching the name given as argument, safely.

The value is passed to execute as a parameter, so the driver escapes
it and an injected statement is treated as plain text.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = %s "
                   "ORDER BY states.id ASC", (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
