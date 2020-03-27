#!/usr/bin/python3
# connect to mysql and list table state

# import modules
import sys
import MySQLdb

if __name__ == '__main__':
    # take arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to the db
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Cursor class
    cursor = db.cursor()
    # Exceute the query
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # fetches all and return list a tuples
    records = cursor.fetchall()
    # print each tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
