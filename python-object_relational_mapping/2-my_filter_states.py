#!/usr/bin/python3
"""Lists all states matching the name given as argument.

This version builds the query with format and is therefore open to
SQL injection. See 3-my_safe_filter_states.py for the safe version.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}' "
                   "ORDER BY states.id ASC".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
