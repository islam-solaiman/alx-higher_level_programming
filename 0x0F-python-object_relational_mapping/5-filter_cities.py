#!/usr/bin/python3

""" Script lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curr = db.cursor()
    curr.execute("""SELECT cities.name FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = curr.fetchall()
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")
    curr.close()
    db.close()
