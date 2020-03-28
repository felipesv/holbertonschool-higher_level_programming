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
    name_inp = sys.argv[4]

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
    sql = "SELECT cities.name\
        FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"
    # Exceute the query
    cursor.execute(sql, (name_inp, ))
    # fetches all and return list a tuples
    records = cursor.fetchall()
    # print name next by ,
    separator = ""
    for row in records:
        print("{}{}".format(separator, row[0]), end="")
        separator = ", "
    if records:
        print("")
    cursor.close()
    db.close()
