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
    # BINARY keyword used to compare using ascii so respect case sensitive
    cr.execute("SELECT * FROM states WHERE BINARY name = '{}' \
            ORDER BY id".format(sys.argv[4]))
    ''' fetchall return tuple of tuples'''
    for row in cr.fetchall():
        print(row)
