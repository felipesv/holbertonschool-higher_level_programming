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
    # create query
    sql = "SELECT cities.id, cities.name, states.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    # Exceute the query
    cursor.execute(sql)
    # fetches all and return list a tuples
    records = cursor.fetchall()
    # print each tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
