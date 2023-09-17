#!/usr/bin/python3
''' get states module '''

import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pswd = sys.argv[2]
    dbs = sys.argv[3]
    search_name = sys.argv[4]
    ht = 'localhost'

    db = MySQLdb.connect(host=ht, port=3306, user=usr, passwd=pswd, db=dbs)
    cr = db.cursor()
    # this approach %s placeholder and tuple or list to get attribute from ( , )
    # is safe from sql injection
    cr.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (search_name, ))
    ''' fetchall return tuple of tuples'''
    for row in cr.fetchall():
        print(row)
