#!/usr/bin/python3
''' get states module '''

import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    dbs = sys.argv[3]
    ht = 'localhost'

    db = MySQLdb.connect(host=ht, port=3306, user=usr, passwd=pswd, db=dbs)
    cr = db.cursor()
    cr.execute("SELECT c.name FROM cities as c \
            INNER JOIN states as s ON c.state_id = s.id \
            WHERE s.name = '{}' \
            ORDER BY c.id".format(sys.argv[4]))
    print(", ".join([row[0] for row in cr.fetchall()]))
