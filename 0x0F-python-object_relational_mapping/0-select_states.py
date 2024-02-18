#!/usr/bin/python3
"""  This lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", username=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    database.close()