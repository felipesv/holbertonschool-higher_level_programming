#!/usr/bin/python3
# connect to mysql and list table state

# import modules
import sys
import MySQLdb

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
sql = "SELECT *\
       FROM states\
       WHERE name = '" + name_inp + "'\
       ORDER BY states.id ASC"
# Exceute the query
cursor.execute(sql)
# fetches all and return list a tuples
records = cursor.fetchall()
# print each tuple
for row in records:
    print(row)
cursor.close()
db.close()
