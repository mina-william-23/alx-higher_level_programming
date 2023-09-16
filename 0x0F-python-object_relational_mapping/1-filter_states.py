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
    cr.execute("SELECT * FROM `states` ORDER BY `id`")
    ''' fetchall return tuple of tuples'''
    for row in cr.fetchall():
        if row[1][0] == 'N':
            print(row)
